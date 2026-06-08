def revenue_trend(df):

    revenue_df = df.copy()

    revenue_df["Month"] = (
        revenue_df["InvoiceDate"]
        .dt.to_period("M")
        .astype(str)
    )

    trend = (
        revenue_df
        .groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    return trend.to_dict(
        orient="records"
    )