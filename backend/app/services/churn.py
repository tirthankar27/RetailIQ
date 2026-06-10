import joblib

MODEL = joblib.load(
    "app/model/churn_model.pkl"
)

FEATURES = [
    "Recency",
    "Frequency",
    "Monetary",
    "AverageOrderValue",
    "CustomerLifetime",
    "AvgDaysBetweenPurchases",
    "UniqueProducts",
    "TotalQuantity"
]


def predict_churn(rfm):

    probabilities = MODEL.predict_proba(
        rfm[FEATURES]
    )[:, 1]

    predictions = (
        probabilities >= 0.5
    ).astype(int)

    rfm["PredictedChurn"] = predictions

    rfm["ChurnProbability"] = probabilities

    high_risk = (
        rfm.sort_values(
            "ChurnProbability",
            ascending=False
        )
        .head(10)
    )

    high_risk_customers = []

    for customer_id, row in high_risk.iterrows():

        high_risk_customers.append(
            {
                "customer_id": int(customer_id),

                "churn_probability": round(
                    row["ChurnProbability"] * 100,
                    2
                )
            }
        )

    return {
        "total_customers":
            len(rfm),

        "predicted_churners":
            int(
                (predictions == 1)
                .sum()
            ),

        "predicted_active":
            int(
                (predictions == 0)
                .sum()
            ),

        "churn_rate":
            round(
                (
                    (predictions == 1)
                    .mean()
                ) * 100,
                2
            ),

        "high_risk_customers":
            high_risk_customers
    }