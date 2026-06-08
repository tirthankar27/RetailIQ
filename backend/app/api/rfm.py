import pandas as pd

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.upload import Upload
from app.models.column_mapping import ColumnMapping

from app.services.data_processor import (
    standardize_dataframe
)

from app.services.rfm import (
    generate_rfm
)

router = APIRouter(
    prefix="/rfm",
    tags=["RFM"]
)

@router.get("/{upload_id}")
def get_rfm(upload_id: int, db: Session = Depends(get_db)):
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
                status_code=404,
                detail="Mapping not found"
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

        rfm = generate_rfm(df)
        return {
            "total_customers":
                int(len(rfm)),

            "average_recency":
                round(
                    rfm["Recency"].mean(),
                    2
                ),

            "average_frequency":
                round(
                    rfm["Frequency"].mean(),
                    2
                ),

            "average_monetary":
                round(
                    rfm["Monetary"].mean(),
                    2
                )
        }