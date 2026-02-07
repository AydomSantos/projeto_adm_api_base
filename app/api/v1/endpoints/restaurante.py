from fastapi import APIRouter, HTTPException
from app.schemas.user_restaurante import UserRestauranteCreateSchema, UserRestauranteSchema, UserRestauranteLoginSchema
from app.services.user_restaurante_service import user_restaurante_service

router = APIRouter()

# Rotas para restaurantes
@router.get("/restaurante/{user_id}", response_model=UserRestauranteSchema)
async def get_user(user_id: int):
    response = user_restaurante_service.get_user_restaurante_by_id(user_id)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return response.data[0]
# As rotas de criação, atualização e exclusão seguem o mesmo padrão, mas usando os métodos do user_restaurante_service
@router.post("/register_restaurante", response_model=UserRestauranteSchema, status_code=201)
async def create_user(user: UserRestauranteCreateSchema):
    response = user_restaurante_service.create_user_restaurante(user.model_dump())
    
    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao criar usuário")
        
    return response.data[0]

@router.put("/update_restaurante/{user_id}", response_model=UserRestauranteSchema)
async def update_user(user_id: int, user: UserRestauranteCreateSchema):
    response = user_restaurante_service.update_user_restaurante(user_id, user.model_dump())
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return response.data[0]

@router.delete("/delete_restaurante/{user_id}")
async def delete_user(user_id: int):
    response = user_restaurante_service.delete_user_restaurante(user_id)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"detail": "Usuário deletado com sucesso"}

@router.post("/login")
async def login(login_data: UserRestauranteLoginSchema):
    # Busca o usuário pelo email
    response = user_restaurante_service.get_user_by_email(login_data.email)
    
    # Verifica se o usuário existe e se a senha confere
    # Nota: Em produção, você deve comparar HASHES de senha, não texto puro.
    if not response.data or response.data[0]["senha"] != login_data.senha:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    user = response.data[0]
    return {"message": "Login realizado com sucesso", "user_id": user["id"], "nome": user["nome"]}