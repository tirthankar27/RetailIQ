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

    result = {"insights": insights}

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    return result