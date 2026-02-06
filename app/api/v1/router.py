from fastapi import APIRouter
from api.v1.endpoints import users

api_router = APIRouter()

# Inclui as rotas de usuários com o prefixo /users
api_router.include_router(users.router, prefix="/users", tags=["Users"])
# Futuramente: api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])