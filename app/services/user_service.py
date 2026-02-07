from app.core.supabase import supabase

class UserService:
    def create_user(self, user_data: dict):
        # A lógica de interação com o banco fica isolada aqui
        response = supabase.table("users").insert(user_data).execute()
        return response

    def get_user_by_id(self, user_id: int):
        response = supabase.table("users").select("*").eq("id", user_id).execute()
        return response

    # Aqui você pode adicionar métodos como update_user, delete_user, etc.

# Instância singleton para ser usada nos endpoints
user_service = UserService()