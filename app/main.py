import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path para evitar erros de importação do módulo 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API configurada com boas práticas em Python/FastAPI",
    version="1.0.0"
)

# --- Configuração de Segurança (CORS) ---
# Define quem pode acessar sua API. Em produção, substitua ["*"] pelos domínios reais.
origins: List[str] = [
    "http://localhost",
    "http://localhost:8080",
    "*" # Cuidado: Permite tudo (útil apenas em dev)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

# --- Registro de Rotas ---
app.include_router(api_router, prefix="/api/v1")

# --- Rotas de Exemplo ---
@app.get("/")
async def health_check():
    return {"status": "ok", "env": settings.ENV}

@app.get("/test-db")
async def test_supabase():
    # Exemplo de consulta ao Supabase
    # Substitua 'sua_tabela' por uma tabela real do seu banco
    # response = supabase.table("users").select("*").limit(1).execute()
    return {"message": "Supabase configurado", "url": settings.SUPABASE_URL}