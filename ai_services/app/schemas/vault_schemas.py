from pydantic import BaseModel, Field

class EncryptRequest(BaseModel):
    plaintext: str = Field(..., min_length=1)

class EncryptResponse(BaseModel):
    ciphertext: str

class DecryptRequest(BaseModel):
    ciphertext: str = Field(..., min_length=1)

class DecryptResponse(BaseModel):
    plaintext: str

class DBRoleRequest(BaseModel):
    role: str = Field(..., min_length=1)

class DBRoleResponse(BaseModel):
    username: str
    password: str
