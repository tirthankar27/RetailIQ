def top_products(
    df,
    limit=10
):

    if "Product" not in df.columns:
        return []

    products = (
        df.groupby("Product")
        ["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(limit)
        .reset_index()
    )

    return products.to_dict(
        orient="records"
    )