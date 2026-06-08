def top_customers(
    df,
    limit=10
):

    top = (
        df.groupby("CustomerID")
        ["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(limit)
        .reset_index()
    )

    return top.to_dict(
        orient="records"
    )