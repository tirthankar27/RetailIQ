import pandas as pd
import json
import os

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

# @router.get("/{upload_id}")
# def get_dashboard(upload_id: int, db: Session = Depends(get_db)):
#     DASHBOARD_REQUESTS.inc()
#     cache_key = (
#         f"dashboard:{upload_id}"
#     )

#     cached = redis_client.get(
#         cache_key
#     )

#     if cached:
#         return json.loads(
#             cached
#         )
    
#     upload = (
#         db.query(Upload)
#         .filter(
#             Upload.id == upload_id
#         )
#         .first()
#     )

#     if not upload:
#         raise HTTPException(
#             404,
#             "Upload not found"
#         )
    
#     mapping = (
#         db.query(ColumnMapping)
#         .filter(
#             ColumnMapping.upload_id
#             == upload_id
#         )
#         .first()
#     )

#     if not mapping:
#         raise HTTPException(
#             404,
#             "Mapping not found"
#         )
    
#     if upload.file_path.endswith(".csv"):
#         df = pd.read_csv(
#             upload.file_path
#         )
#     else:
#         df = pd.read_excel(
#             upload.file_path
#         )
    
#     df = standardize_dataframe(
#         df,
#         mapping
#     )

#     result = generate_dashboard(df)
    
#     rfm = generate_rfm(
#         df
#     )

#     prediction = predict_churn(
#         rfm
#     )

#     result["predicted_churners"] = (
#         prediction["predicted_churners"]
#     )

#     result["churn_rate"] = (
#         prediction["churn_rate"]
#     )

#     redis_client.setex(
#         cache_key,
#         CACHE_TTL,
#         json.dumps(result)
#     )

#     return result

@router.get("/{upload_id}")
def get_dashboard(upload_id: int, db: Session = Depends(get_db)):
    print("STEP 1")

    DASHBOARD_REQUESTS.inc()

    cache_key = f"dashboard:{upload_id}"

    print("STEP 2")

    cached = redis_client.get(cache_key)

    if cached:
        print("CACHE HIT")
        return json.loads(cached)

    print("STEP 3")

    upload = (
        db.query(Upload)
        .filter(Upload.id == upload_id)
        .first()
    )

    print("STEP 4")

    mapping = (
        db.query(ColumnMapping)
        .filter(ColumnMapping.upload_id == upload_id)
        .first()
    )

    print("STEP 5")

    print(upload.file_path, flush=True)
    print(os.path.exists(upload.file_path), flush=True)
    print(os.path.getsize(upload.file_path), flush=True)
    if upload.file_path.endswith(".csv"):
        df = pd.read_csv(upload.file_path)
    else:
        df = pd.read_excel(upload.file_path)

    print("STEP 6")

    df = standardize_dataframe(df, mapping)

    print("STEP 7")

    result = generate_dashboard(df)

    print("STEP 8")

    rfm = generate_rfm(df)

    print("STEP 9")

    prediction = predict_churn(rfm)

    print("STEP 10")

    result["predicted_churners"] = prediction["predicted_churners"]
    result["churn_rate"] = prediction["churn_rate"]

    print("STEP 11")

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(result)
    )

    print("STEP 12")

    return result