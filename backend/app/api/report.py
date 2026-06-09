from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import (
    FileResponse
)

from sqlalchemy.orm import Session

import os

from app.database.dependencies import get_db

from app.models.upload import Upload
from app.models.column_mapping import ColumnMapping
from app.services.metrics import (REPORT_DOWNLOADS)

from app.services.dataset_loader import (
    load_standardized_df
)

from app.services.report_generator import (
    generate_report
)

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.get("/{upload_id}")
def download_report(
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

    dashboard = {
        "kpis": {
            "revenue": float(
                df["Revenue"].sum()
            ),

            "orders": int(
                len(df)
            ),

            "customers": int(
                df["CustomerID"]
                .nunique()
            ),

            "average_order_value": float(
                df["Revenue"].mean()
            )
        }
    }

    insights = []

    insights.append(
        f"Total revenue generated is {dashboard['kpis']['revenue']:,.2f}"
    )

    insights.append(
        f"The business served {dashboard['kpis']['customers']} unique customers."
    )

    top_customer = (
        df.groupby("CustomerID")
        ["Revenue"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Customer {int(top_customer)} generated the highest revenue."
    )

    if "Product" in df.columns:

        top_product = (
            df.groupby("Product")
            ["Revenue"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Top revenue-generating product is '{top_product}'."
        )

    os.makedirs(
        "reports",
        exist_ok=True
    )

    pdf_path = (
        f"reports/report_{upload_id}.pdf"
    )

    top_customers = (
        df.groupby("CustomerID")
        ["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    top_products = (
        df.groupby("Product")
        ["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    generate_report(
        pdf_path,
        dashboard,
        insights,
        top_customers,
        top_products
    )

    REPORT_DOWNLOADS.inc()

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"report_{upload_id}.pdf"
    )