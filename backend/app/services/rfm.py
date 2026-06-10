import pandas as pd


def generate_rfm(df):

    snapshot_date = (
        df["InvoiceDate"].max()
        + pd.Timedelta(days=1)
    )

    rfm = (
        df.groupby("CustomerID")
        .agg(
            Recency=(
                "InvoiceDate",
                lambda x: (
                    snapshot_date
                    - x.max()
                ).days
            ),

            Frequency=(
                "InvoiceDate",
                "count"
            ),

            Monetary=(
                "Revenue",
                "sum"
            ),

            TotalQuantity=(
                "Quantity",
                "sum"
            ),

            FirstPurchase=(
                "InvoiceDate",
                "min"
            ),

            LastPurchase=(
                "InvoiceDate",
                "max"
            )
        )
    )

    rfm["CustomerLifetime"] = (
        rfm["LastPurchase"]
        - rfm["FirstPurchase"]
    ).dt.days + 1

    rfm["AverageOrderValue"] = (
        rfm["Monetary"]
        / rfm["Frequency"]
    )

    rfm["AvgDaysBetweenPurchases"] = (
        rfm["CustomerLifetime"]
        / rfm["Frequency"]
    )

    unique_products = (
        df.groupby("CustomerID")
        ["Product"]
        .nunique()
    )

    rfm["UniqueProducts"] = (
        unique_products
    )

    rfm.drop(
        columns=[
            "FirstPurchase",
            "LastPurchase"
        ],
        inplace=True
    )

    return rfm