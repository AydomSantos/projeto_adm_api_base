from fastapi import APIRouter
from app.api.v1.endpoints import users, fornecedor, restaurante, produto

api_router = APIRouter()

# Inclui as rotas de usuários com o prefixo /users
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(fornecedor.router, prefix="/auth", tags=["Fornecedores"])
api_router.include_router(restaurante.router, prefix="/auth", tags=["Restaurantes"])
api_router.include_router(produto.router, prefix="/produtos", tags=["Produtos"])