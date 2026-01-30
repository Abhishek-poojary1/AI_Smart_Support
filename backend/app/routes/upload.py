from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.ingestion import ingest_document

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_document(file_path)

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename
    }
