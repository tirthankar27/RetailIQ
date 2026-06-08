from pydantic import BaseModel


class MappingCreate(BaseModel):
    customer_column: str
    date_column: str
    quantity_column: str
    price_column: str
    product_column: str | None = None