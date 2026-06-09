import pandas as pd
import json

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.models.upload import Upload
from app.models.column_mapping import ColumnMapping
from app.services.cache import redis_client

from app.database.dependencies import get_db

from app.services.analytics import (
    generate_basic_kpis
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/{upload_id}")
def analytics(upload_id: int, db: Session = Depends(get_db)):
    cache_key = f"analytics:{upload_id}"

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

    if not upload:
        raise HTTPException(
            404,
            "Upload not found"
        )
    
    mapping = (
        db.query(ColumnMapping)
        .filter(
            ColumnMapping.upload_id
            == upload_id
        )
        .first()
    )

    if not mapping:
        raise HTTPException(
            400,
            "Mapping not found"
        )
    
    if upload.file_path.endswith(".csv"):
        df = pd.read_csv(
            upload.file_path
        )
    else:
        df = pd.read_excel(
            upload.file_path
        )
    
    df = df.rename(
        columns={
            mapping.customer_column:
                "CustomerID",

            mapping.date_column:
                "InvoiceDate",

            mapping.quantity_column:
                "Quantity",

            mapping.price_column:
                "UnitPrice"
        }
    )

    result = generate_basic_kpis(df)

    redis_client.setex(
        cache_key,
        3600,
        json.dumps(result)
    )

    return result