from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def generate_pdf_report(
    transaction: dict,
    prediction_result: dict,
) -> BytesIO:
    """
    Generate a fraud investigation PDF report.
    Returns an in-memory BytesIO buffer.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    elements = []

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------
    title = Paragraph(
        "<b>FraudShield AI - Investigation Report</b>",
        styles["Title"],
    )
    elements.append(title)
    elements.append(Spacer(1, 20))

    # -----------------------------------------------------
    # Summary Table
    # -----------------------------------------------------
    summary_data = [
        ["Metric", "Value"],
        ["Fraud Probability", f"{prediction_result['fraud_probability']:.6f}"],
        ["Anomaly Score", f"{prediction_result['anomaly_score']:.6f}"],
        ["Risk Score", str(prediction_result["risk_score"])],
        ["Severity", prediction_result["severity"]],
        ["Predicted Fraud", str(prediction_result["is_fraud"])],
    ]

    summary_table = Table(summary_data, colWidths=[200, 250])
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f2937")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1),
                 [colors.whitesmoke, colors.beige]),
            ]
        )
    )

    elements.append(summary_table)
    elements.append(Spacer(1, 20))

    # -----------------------------------------------------
    # Key Risk Factors
    # -----------------------------------------------------
    elements.append(
        Paragraph("<b>Key Risk Factors</b>", styles["Heading2"])
    )

    for factor in prediction_result["key_risk_factors"]:
        text = (
            f"{factor['feature']}: "
            f"{factor['impact']:+.4f}"
        )
        elements.append(Paragraph(text, styles["BodyText"]))

    elements.append(Spacer(1, 20))

    # -----------------------------------------------------
    # Recommended Actions
    # -----------------------------------------------------
    elements.append(
        Paragraph("<b>Recommended Actions</b>", styles["Heading2"])
    )

    for recommendation in prediction_result["recommendations"]:
        elements.append(
            Paragraph(f"• {recommendation}", styles["BodyText"])
        )

    elements.append(Spacer(1, 20))

    # -----------------------------------------------------
    # Transaction Summary
    # -----------------------------------------------------
    elements.append(
        Paragraph("<b>Transaction Summary</b>", styles["Heading2"])
    )

    # Show only a few relevant fields
    summary_fields = ["Time", "Amount"]

    for field in summary_fields:
        if field in transaction:
            elements.append(
                Paragraph(
                    f"{field}: {transaction[field]}",
                    styles["BodyText"],
                )
            )

    # -----------------------------------------------------
    # Build PDF
    # -----------------------------------------------------
    doc.build(elements)

    buffer.seek(0)
    return buffer