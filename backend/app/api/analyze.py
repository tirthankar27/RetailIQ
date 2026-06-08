from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import pandas as pd

from app.database.dependencies import get_db
from app.models.upload import Upload
from app.services.schema_detector import detect_columns

router = APIRouter(
    prefix="/analyze",
    tags=["Analyze"]
)

@router.get("/{upload_id}")
def analyze_file(
    upload_id: int,
    db: Session = Depends(get_db)
):

    upload = (
        db.query(Upload)
        .filter(
            Upload.id == upload_id
        )
        .first()
    )

    if not upload:
        raise HTTPException(
            status_code=404,
            detail="Upload not found"
        )

    file_path = upload.file_path

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    else:
        df = pd.read_excel(file_path)

    return {
        "columns": list(df.columns),

        "preview": (
            df.head(10)
            .fillna("")
            .to_dict(
                orient="records"
            )
        ),

        "suggested_mapping":
            detect_columns(
                list(df.columns)
            )
    }