import pandas as pd
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
from app.services.cache import (redis_client, CACHE_TTL)

from app.services.data_processor import (
    standardize_dataframe
)

from app.services.revenue import (
    revenue_trend
)

router = APIRouter(
    prefix="/revenue",
    tags=["Revenue"]
)

@router.get("/{upload_id}")
def get_revenue_trend(upload_id: int, db: Session = Depends(get_db)):
    cache_key = (
        f"revenue:{upload_id}"
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
    
    if upload.file_path.endswith(".csv"):
        df = pd.read_csv(
            upload.file_path
        )
    else:
        df = pd.read_excel(
            upload.file_path
        )
    
    df = standardize_dataframe(
        df,
        mapping
    )

    result = revenue_trend(df)

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    return result