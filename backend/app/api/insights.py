from fastapi import (
    APIRouter,
    Depends
)
import json

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.upload import Upload
from app.models.column_mapping import ColumnMapping
from app.services.cache import (redis_client, CACHE_TTL)
from app.services.rfm import (
    generate_rfm
)

from app.services.churn import (
    predict_churn
)

from app.services.dataset_loader import (
    load_standardized_df
)

router = APIRouter(
    prefix="/insights",
    tags=["Insights"]
)

@router.get("/{upload_id}")
def generate_insights(upload_id: int, db: Session = Depends(get_db)):

    cache_key = (
        f"insights:{upload_id}"
    )

    cached = redis_client.get(
        cache_key
    )

    if cached:
        return json.loads(
            cached
        )

    upload = (
        db.query(Upload)
        .filter(
            Upload.id == upload_id
        )
        .first()
    )

    mapping = (
        db.query(ColumnMapping)
        .filter(
            ColumnMapping.upload_id
            == upload_id
        )
        .first()
    )

    df = load_standardized_df(
        upload,
        mapping
    )

    insights = []

    total_revenue = (
        df["Revenue"]
        .sum()
    )

    insights.append(
        f"Total revenue generated is ₹{total_revenue:,.2f}"
    )

    total_customers = (
        df["CustomerID"]
        .nunique()
    )

    insights.append(
        f"The business served {total_customers} unique customers."
    )

    top_customer = (
        df.groupby("CustomerID")
        ["Revenue"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Customer {top_customer} generated the highest revenue."
    )

    if "Product" in df.columns:

        top_product = (
            df.groupby("Product")
            ["Revenue"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Top revenue-generating product is '{top_product}'."
        )
    
    rfm = generate_rfm(
        df
    )

    prediction = predict_churn(
        rfm
    )

    insights.append(
        f"Predicted churn rate is {prediction['churn_rate']}%."
    )

    insights.append(
        f"{prediction['predicted_churners']} customers are at risk of churn."
    )

    result = {"insights": insights}

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    return result