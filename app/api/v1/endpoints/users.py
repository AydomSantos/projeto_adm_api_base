from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserResponse
from services.user_service import user_service

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    # Chama o serviço em vez de acessar o banco diretamente
    response = user_service.create_user(user.model_dump())
    
    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao criar usuário")
        
    return response.data[0]

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    response = user_service.get_user_by_id(user_id)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return response.data[0]