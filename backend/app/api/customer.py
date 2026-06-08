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

from app.services.customer import (
    top_customers
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/top/{upload_id}")
def get_top_customers(
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

    return top_customers(df)