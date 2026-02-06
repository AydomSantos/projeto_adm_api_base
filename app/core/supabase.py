from supabase import create_client, Client
from core.config import settings

# Inicializa o cliente Supabase usando as configurações validadas
def get_supabase_client() -> Client:
    url: str = settings.SUPABASE_URL
    key: str = settings.SUPABASE_KEY
    
    if not url or not key:
        raise ValueError("Supabase URL e Key são obrigatórios no arquivo .env")
        
    return create_client(url, key)

supabase = get_supabase_client()
