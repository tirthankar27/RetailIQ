from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib import colors
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_report(
    filepath,
    dashboard,
    insights,
    top_customers,
    top_products,
    high_risk_customers,
    revenue_data
):

    doc = SimpleDocTemplate(
        filepath
    )

    styles = (
        getSampleStyleSheet()
    )

    title_style = styles["Title"]

    title_style.textColor = (
        colors.HexColor("#2563EB")
    )

    content = []

    content.append(
        Paragraph(
            "RetailIQ Executive Report",
            title_style
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    kpi_table = Table(
        [
            [
                "Revenue",
                "Orders"
            ],
            [
                f"Rs. {dashboard['kpis']['revenue']:,.2f}",
                f"{dashboard['kpis']['orders']:,}"
            ],
            [
                "Customers",
                "AOV"
            ],
            [
                f"{dashboard['kpis']['customers']:,}",
                f"Rs. {dashboard['kpis']['average_order_value']:,.2f}"
            ]
        ],
        colWidths=[220, 220]
    )

    kpi_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.HexColor("#DBEAFE")
            ),
            (
                "BACKGROUND",
                (0,2),
                (-1,2),
                colors.HexColor("#DBEAFE")
            ),
            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                colors.grey
            ),
            (
                "FONTNAME",
                (0,0),
                (-1,0),
                "Helvetica-Bold"
            ),
            (
                "FONTNAME",
                (0,2),
                (-1,2),
                "Helvetica-Bold"
            ),
            (
                "ALIGN",
                (0,0),
                (-1,-1),
                "CENTER"
            ),
        ])
    )

    content.append(kpi_table)

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            "Key Business Insights",
            styles["Heading2"]
        )
    )

    for insight in insights:
        insight_box = Table(
            [[f"• {insight}"]],
            colWidths=[450]
        )

        insight_box.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0,0),
                    (-1,-1),
                    colors.HexColor("#EFF6FF")
                ),
                (
                    "BOX",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.HexColor("#BFDBFE")
                ),
                (
                    "PADDING",
                    (0,0),
                    (-1,-1),
                    10
                ),
            ])
        )

        content.append(insight_box)
        content.append(
            Spacer(
                1,
                20
            )
        )

    content.append(
        Paragraph(
            "Top Customers",
            styles["Heading2"]
        )
    )

    customer_data = [
        [
            "Customer ID",
            "Revenue"
        ]
    ]

    for _, row in (
        top_customers.iterrows()
    ):

        customer_data.append(
            [
                str(
                    int(
                        row["CustomerID"]
                    )
                ),
                f"Rs. {row['Revenue']:,.2f}"
            ]
        )

    customer_table = Table(
        customer_data,
        colWidths=[200, 250]
    )

    customer_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.HexColor(
                    "#DBEAFE"
                )
            ),
            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                colors.grey
            ),
            (
                "FONTNAME",
                (0,0),
                (-1,0),
                "Helvetica-Bold"
            )
        ])
    )

    content.append(
        customer_table
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            "Top Products",
            styles["Heading2"]
        )
    )

    product_data = [
        [
            "Product",
            "Revenue"
        ]
    ]

    for _, row in (
        top_products.iterrows()
    ):

        product_data.append(
            [
                str(
                    row["Product"]
                )[:40],
                f"Rs. {row['Revenue']:,.2f}"
            ]
        )

    product_table = Table(
        product_data,
        colWidths=[300, 150]
    )
    product_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.HexColor(
                    "#DCFCE7"
                )
            ),
            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                colors.grey
            ),
            (
                "FONTNAME",
                (0,0),
                (-1,0),
                "Helvetica-Bold"
            )
        ])
    )

    content.append(
        product_table
    )

    content.append(
        Spacer(
            1,
            6
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            "Top Customers Likely To Churn",
            styles["Heading2"]
        )
    )

    churn_data = [
        [
            "Customer ID",
            "Churn Probability (%)"
        ]
    ]

    for customer in high_risk_customers:

        churn_data.append(
            [
                str(
                    customer["customer_id"]
                ),

                f"{customer['churn_probability']}%"
            ]
        )

    churn_table = Table(
        churn_data,
        colWidths=[220, 220]
    )

    churn_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.HexColor(
                    "#FEE2E2"
                )
            ),
            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                colors.grey
            ),
            (
                "FONTNAME",
                (0,0),
                (-1,0),
                "Helvetica-Bold"
            )
        ])
    )

    content.append(
        churn_table
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    months = [
        row["Month"]
        for row in revenue_data
    ]

    revenues = [
        row["Revenue"]
        for row in revenue_data
    ]

    plt.figure(
        figsize=(6,3)
    )

    plt.plot(
        months,
        revenues,
        linewidth=3,
        marker="o"
    )

    plt.title(
        "Revenue Trend"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    chart_path = (
        filepath.replace(
            ".pdf",
            "_chart.png"
        )
    )

    plt.savefig(
        chart_path
    )

    plt.close()

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            "Revenue Trend",
            styles["Heading2"]
        )
    )

    content.append(
        Image(
            chart_path,
            width=450,
            height=220
        )
    )

    doc.build(
        content
    )