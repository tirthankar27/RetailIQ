import pandas as pd


def assign_segment(row):

    if row["R"] >= 4 and row["F"] >= 4:
        return "Champions"

    elif row["R"] >= 3 and row["F"] >= 3:
        return "Loyal Customers"

    elif row["R"] >= 3 and row["F"] <= 2:
        return "Potential Loyalists"

    elif row["R"] <= 2 and row["F"] >= 3:
        return "At Risk"

    return "Others"


def generate_segments(rfm):

    rfm["R"] = pd.qcut(
        rfm["Recency"],
        4,
        labels=[4, 3, 2, 1],
        duplicates="drop"
    )

    rfm["F"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        4,
        labels=[1, 2, 3, 4],
        duplicates="drop"
    )

    rfm["Segment"] = rfm.apply(
        assign_segment,
        axis=1
    )

    return rfm