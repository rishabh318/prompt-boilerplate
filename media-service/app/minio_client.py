import boto3
from botocore.client import Config
from app.config import settings

session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    endpoint_url=f"http{'s' if settings.USE_SSL else ''}://{settings.MINIO_ENDPOINT}",
    aws_access_key_id=settings.MINIO_ACCESS_KEY,
    aws_secret_access_key=settings.MINIO_SECRET_KEY,
    config=Config(signature_version='s3v4'),
    verify=settings.USE_SSL
)

def ensure_bucket_exists(bucket_name: str):
    existing_buckets = s3_client.list_buckets()
    if not any(bucket["Name"] == bucket_name for bucket in existing_buckets.get("Buckets", [])):
        s3_client.create_bucket(Bucket=bucket_name)
