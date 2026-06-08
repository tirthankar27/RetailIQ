from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)
import os
import shutil
from app.models.upload import Upload
from sqlalchemy.orm import Session
from pathlib import Path
from app.database.dependencies import get_db

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx",
        ".xls"
    }
    extension = Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only CSV, XLSX and XLS files are allowed"
        )

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    upload = Upload(
        filename=file.filename,
        file_path=file_path
    )

    db.add(upload)

    db.commit()

    db.refresh(upload)

    return {
        "id": upload.id,
        "filename": upload.filename,
        "status": upload.status
    }