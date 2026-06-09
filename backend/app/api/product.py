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
    prefix="/products",
    tags=["Products"]
)

@router.get("/top/{upload_id}")
def top_products(upload_id: int, db: Session = Depends(get_db)):
    cache_key = (
        f"products:{upload_id}"
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

    if "Product" not in df.columns:
        return []

    result = (
        df.groupby("Product")
        ["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    result = result.to_dict(orient="records")

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    return result