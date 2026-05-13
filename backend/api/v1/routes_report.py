from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.api.schemas.prediction import PredictionRequest
from backend.services.pdf_report import generate_pdf_report
from backend.services.prediction_service import predict_transaction

router = APIRouter()


@router.post(
    "/report/pdf",
    responses={
        200: {
            "content": {
                "application/pdf": {}
            },
            "description": "PDF fraud investigation report",
        }
    },
)
def generate_report(request: PredictionRequest):
    """
    Generate a downloadable PDF fraud investigation report.
    """

    # Convert request to dictionary
    transaction = request.model_dump()

    # Run fraud prediction
    prediction_result = predict_transaction(transaction)

    # Generate PDF in memory
    pdf_buffer = generate_pdf_report(
        transaction=transaction,
        prediction_result=prediction_result,
    )

    # Optional debug: save a local copy to verify generation
    with open("test_report.pdf", "wb") as f:
        f.write(pdf_buffer.getvalue())

    # Reset buffer pointer after writing to disk
    pdf_buffer.seek(0)

    # Return downloadable PDF
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": (
                "attachment; filename=fraud_report.pdf"
            )
        },
    )