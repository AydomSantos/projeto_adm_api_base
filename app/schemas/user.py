from pydantic import BaseModel, EmailStr
from typing import Optional

# Modelo para receber dados (Criação)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Modelo para retornar dados (Leitura)
class UserResponse(UserCreate):
    id: int
    
    class Config:
        from_attributes = True