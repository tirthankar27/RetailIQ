import pandas as pd


def generate_basic_kpis(df):

    revenue = (
        df["Quantity"] *
        df["UnitPrice"]
    ).sum()

    total_orders = len(df)

    total_customers = (
        df["CustomerID"]
        .nunique()
    )

    avg_order_value = (
        revenue / total_orders
        if total_orders
        else 0
    )

    return {
        "revenue": float(revenue),
        "orders": int(total_orders),
        "customers": int(total_customers),
        "average_order_value": round(
            avg_order_value,
            2
        )
    }