from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # Define as variáveis esperadas
    SUPABASE_URL: str
    SUPABASE_KEY: str
    PORT: int = 3000
    
    # Configurações adicionais
    ENV: str = "development"
    PROJECT_NAME: str = "Projeto Adm API"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Cache para não ler o arquivo .env a cada requisição
@lru_cache
def get_settings():
    return Settings()

# Instância global
settings = get_settings()