from app.services.analytics import (
    generate_basic_kpis
)

from app.services.rfm import (
    generate_rfm
)

from app.services.segmentation import (
    generate_segments
)


def generate_dashboard(df):

    kpis = generate_basic_kpis(df)

    rfm = generate_rfm(df)

    segmented_rfm = generate_segments(
        rfm.copy()
    )

    segment_counts = (
        segmented_rfm["Segment"]
        .value_counts()
        .to_dict()
    )

    rfm_summary = {
        "total_customers":
            int(len(rfm)),

        "average_recency":
            round(
                rfm["Recency"].mean(),
                2
            ),

        "average_frequency":
            round(
                rfm["Frequency"].mean(),
                2
            ),

        "average_monetary":
            round(
                rfm["Monetary"].mean(),
                2
            )
    }

    return {
        "kpis": kpis,
        "rfm_summary": rfm_summary,
        "segments": segment_counts
    }