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
from app.services.metrics import (DASHBOARD_REQUESTS)
from app.services.dataset_loader import (load_standardized_df)
from app.services.rfm import generate_rfm

from app.services.churn import (
    predict_churn
)

from app.services.data_processor import (
    standardize_dataframe
)

from app.services.dashboard import (
    generate_dashboard
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/{upload_id}")
def get_dashboard(upload_id: int, db: Session = Depends(get_db)):
    DASHBOARD_REQUESTS.inc()
    cache_key = (
        f"dashboard:{upload_id}"
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

    result = generate_dashboard(df)
    
    rfm = generate_rfm(
        df
    )

    prediction = predict_churn(
        rfm
    )

    result["predicted_churners"] = (
        prediction["predicted_churners"]
    )

    result["churn_rate"] = (
        prediction["churn_rate"]
    )

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    return result