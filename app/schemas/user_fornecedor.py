# importações necessarias 
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum

# Enum para status do usuário
class UserStatus(str, Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"
    PENDENTE = "pendente"
    BLOQUEADO = "bloqueado"
    SUSPENSO = "suspenso"

# Model de criação do perfil do tipo fornecedor 
class UserFornecedorCreateSchema(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr = Field(..., max_length=255)
    senha: str = Field(..., min_length=6, max_length=128)
    numero: int = Field(..., gt=0)
    cnpj: str = Field(..., min_length=14, max_length=14)

    @validator('cnpj')
    def validar_cnpj(cls, v):
        if not v.isdigit():
            raise ValueError('CNPJ deve conter apenas números')
        if len(v) != 14:
            raise ValueError('CNPJ deve conter exatamente 14 dígitos')
        return v

# Model de resposta do perfil do tipo fornecedor, inclui o ID gerado automaticamente
class UserFornecedorSchema(UserFornecedorCreateSchema):
    id: int
    status: UserStatus 
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_encoders = {
             "example": {
                "id": 1,
                "nome": "Empresa Ltda",
                "email": "fornecedor@empresa.com",
                "numero": 11987654321,
                "cnpj": "12345678000190",
                "status": "active",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-01T00:00:00",
                "last_login": None
            }
        }
    
# Model de login do perfil do tipo fornecedor
class UserFornecedorLoginSchema(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    senha: str = Field(..., min_length=6, max_length=128)

# Model de atualização do perfil do tipo fornecedor
class UserFornecedorUpdateSchema(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    senha: Optional[str] = Field(None, min_length=6, max_length=128)
    numero: Optional[int] = Field(None, gt=0)
    cnpj: Optional[str] = Field(None, min_length=14, max_length=14)
    
# Model de resposta do login do perfil do tipo fornecedor, inclui o token de acesso
class SessionSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Model de resposta de sucesso para operações relacionadas ao perfil do tipo fornecedor
class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Optional[dict] = None

# Model de resposta de erro para operações relacionadas ao perfil do tipo fornecedor
class ErrorResponse(BaseModel):
    success: bool = False
    error_code: Optional[int] = None
    message: str
    data: Optional[dict] = None
