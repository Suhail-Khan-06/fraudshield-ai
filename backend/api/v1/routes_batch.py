from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.services.batch_service import analyze_csv

router = APIRouter()


@router.post("/predict/csv")
async def predict_csv(file: UploadFile = File(...)):
    """
    Perform batch fraud analysis on an uploaded CSV file.
    """

    # Validate file extension
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported.",
        )

    try:
        file_bytes = await file.read()
        result = analyze_csv(file_bytes)
        return result

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Batch analysis failed: {str(exc)}",
        )