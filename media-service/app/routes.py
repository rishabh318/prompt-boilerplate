from fastapi import APIRouter, UploadFile, File, HTTPException
from app.minio_client import s3_client, ensure_bucket_exists
from app.config import settings
import uuid
import mimetypes
import io
from fastapi.responses import StreamingResponse
import botocore.exceptions

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    allowed_types = ["image/jpeg", "image/png", "video/mp4"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    unique_name = f"{uuid.uuid4()}-{file.filename}"
    contents = await file.read()

    ensure_bucket_exists(settings.MINIO_BUCKET)
    
    s3_client.put_object(
        Bucket=settings.MINIO_BUCKET,
        Key=unique_name,
        Body=contents,
        ContentType=file.content_type
    )

    file_url = f"http://{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET}/{unique_name}"
    return {"filename": unique_name, "url": file_url}


@router.get("/media/{filename}")
def get_file(filename: str):
    try:
        response = s3_client.get_object(
            Bucket=settings.MINIO_BUCKET,
            Key=filename
        )

        # Read the file data from MinIO
        file_data = response['Body'].read()
        content_type = response['ContentType']

        return StreamingResponse(io.BytesIO(file_data), media_type=content_type)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise HTTPException(status_code=404, detail="File not found in bucket.")
        else:
            raise HTTPException(status_code=500, detail="Error accessing MinIO.")