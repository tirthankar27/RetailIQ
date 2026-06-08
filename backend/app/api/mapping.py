from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.column_mapping import ColumnMapping
from app.schemas.column_mapping import MappingCreate

router = APIRouter(
    prefix="/mapping",
    tags=["Mapping"]
)

@router.post("/{upload_id}")
def save_mapping(
    upload_id: int,
    mapping: MappingCreate,
    db: Session = Depends(get_db)
):

    row = ColumnMapping(
        upload_id=upload_id,
        customer_column=mapping.customer_column,
        date_column=mapping.date_column,
        quantity_column=mapping.quantity_column,
        price_column=mapping.price_column,
        product_column=mapping.product_column
    )

    db.add(row)
    db.commit()

    return {
        "message": "mapping saved"
    }