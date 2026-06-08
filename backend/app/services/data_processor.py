import pandas as pd


def standardize_dataframe(df, mapping):

    rename_map = {
        mapping.customer_column: "CustomerID",
        mapping.date_column: "InvoiceDate",
        mapping.quantity_column: "Quantity",
        mapping.price_column: "UnitPrice"
    }

    if (hasattr(mapping, "product_column") and mapping.product_column):
        rename_map[
            mapping.product_column
        ] = "Product"

    df = df.rename(columns=rename_map)

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    df["UnitPrice"] = pd.to_numeric(
        df["UnitPrice"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "CustomerID",
            "InvoiceDate",
            "Quantity",
            "UnitPrice"
        ]
    )

    df["Revenue"] = (
        df["Quantity"] *
        df["UnitPrice"]
    )

    return df