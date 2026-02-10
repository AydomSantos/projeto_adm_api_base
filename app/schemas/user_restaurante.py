# Schemas para o perfil do tipo restaurante
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

# Enum para status do usuário
class UserRestauranteCreateSchema(BaseModel):
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

# Model de resposta do perfil do tipo restaurante, inclui o ID gerado automaticamente
class UserRestauranteSchema(UserRestauranteCreateSchema):
    id: int

    class Config:
        from_attributes = True

# Model de login do perfil do tipo restaurante
class UserRestauranteLoginSchema(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    senha: str = Field(..., min_length=6, max_length=128)

# Model de resposta do login do perfil do tipo restaurante, inclui o token de acesso
class SessionSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Model de atualização do perfil do tipo restaurante
class UserRestauranteUpdateSchema(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    senha: Optional[str] = Field(None, min_length=6, max_length=128)
    numero: Optional[int] = Field(None, gt=0)
    cnpj: Optional[str] = Field(None, min_length=14, max_length=14)

    @validator('cnpj')
    def validar_cnpj(cls, v):
        if v is not None:
            if not v.isdigit():
                raise ValueError('CNPJ deve conter apenas números')
            if len(v) != 14:
                raise ValueError('CNPJ deve conter exatamente 14 dígitos')
        return v

# Model de resposta genérica para operações bem-sucedidas
class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Optional[dict] = None

# Model de resposta genérica para operações que falharam
class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    details: Optional[dict] = None

# Model de resposta genérica para operações que falharam
class UserStatus(str):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    blocked = "blocked"
    suspended = "suspended"

# Model de resposta para solicitação de redefinição de senha
class PasswordResetRequestSchema(BaseModel):
    email: EmailStr = Field(..., max_length=255)
# Model de resposta para solicitação de redefinição de senha
class PasswordResetSchema(BaseModel):
    token: str
    nova_senha: str = Field(..., min_length=6, max_length=128)

# Model de resposta para verificação de email
class EmailVerificationSchema(BaseModel):
    token: str