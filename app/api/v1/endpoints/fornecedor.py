from fastapi import APIRouter, HTTPException
from app.schemas.user_fornecedor import UserFornecedorCreateSchema, UserFornecedorSchema, UserFornecedorLoginSchema
from app.services.user_fornecedor import user_fornecedor_service

router = APIRouter()

# Rotas para fornecedores
@router.get("/fornecedor/{user_id}", response_model=UserFornecedorSchema)
async def get_user(user_id: int):
    response = user_fornecedor_service.get_user_fornecedor_by_id(user_id)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return response.data[0]

# As rotas de criação, atualização e exclusão seguem o mesmo padrão, mas usando os métodos do user_fornecedor_service
@router.post("/register_fornecedor", response_model=UserFornecedorSchema, status_code=201)
async def create_user(user: UserFornecedorCreateSchema):
    response = user_fornecedor_service.create_user_fornecedor(user.model_dump())
    
    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao criar usuário")
        
    return response.data[0]

# As rotas de atualização e exclusão seguem o mesmo padrão, mas usando os métodos do user_fornecedor_service
@router.put("/update_fornecedor/{user_id}", response_model=UserFornecedorSchema)
async def update_user(user_id: int, user: UserFornecedorCreateSchema):
    response = user_fornecedor_service.update_user_fornecedor(user_id, user.model_dump())
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return response.data[0]

@router.delete("/delete_fornecedor/{user_id}")
async def delete_user(user_id: int):
    response = user_fornecedor_service.delete_user_fornecedor(user_id)
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"detail": "Usuário deletado com sucesso"}

@router.post("/login")
async def login(login_data: UserFornecedorLoginSchema):
    # Busca o usuário pelo email
    response = user_fornecedor_service.get_user_by_email(login_data.email)
    
    # Verifica se o usuário existe e se a senha confere
    # Nota: Em produção, você deve comparar HASHES de senha, não texto puro.
    if not response.data or response.data[0]["senha"] != login_data.senha:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    user = response.data[0]
    return {"message": "Login realizado com sucesso", "user_id": user["id"], "nome": user["nome"]}