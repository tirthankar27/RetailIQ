import json

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.upload import Upload
from app.models.column_mapping import ColumnMapping
from app.services.dataset_loader import (load_standardized_df)
from app.services.cache import (redis_client, CACHE_TTL)

from app.services.data_processor import (
    standardize_dataframe
)

from app.services.customer import (
    top_customers
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/top/{upload_id}")
def get_top_customers(upload_id: int, db: Session = Depends(get_db)):
    cache_key = (
        f"top_customers:{upload_id}"
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
            404,
            "Mapping not found"
        )

    df = load_standardized_df(
        upload,
        mapping
    )

    result = top_customers(df)

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    return result