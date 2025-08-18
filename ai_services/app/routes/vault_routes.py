from fastapi import APIRouter, HTTPException
from app.schemas.vault_schemas import (
    EncryptRequest, EncryptResponse,
    DecryptRequest, DecryptResponse,
    DBRoleRequest, DBRoleResponse
)
from app.services import vault_service

router = APIRouter(prefix="/vault", tags=["Vault"])

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/encrypt", response_model=EncryptResponse)
def encrypt(req: EncryptRequest):
    try:
        ciphertext = vault_service.encrypt_text(req.plaintext)
        return EncryptResponse(ciphertext=ciphertext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/decrypt", response_model=DecryptResponse)
def decrypt(req: DecryptRequest):
    try:
        plaintext = vault_service.decrypt_text(req.ciphertext)
        return DecryptResponse(plaintext=plaintext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rotate", status_code=204)
def rotate():
    try:
        vault_service.rotate_key()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/db-creds", response_model=DBRoleResponse)
def get_db_creds(req: DBRoleRequest):
    try:
        creds = vault_service.fetch_db_creds(req.role)
        return DBRoleResponse(username=creds["username"], password=creds["password"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
