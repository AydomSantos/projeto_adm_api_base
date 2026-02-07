from app.core.supabase import supabase

class UserRestauranteService:
    def create_user_restaurante(self, user_data: dict):
        response = supabase.table("user_restaurante").insert(user_data).execute()
        return response
    
    def get_user_restaurante_by_id(self, user_id: int):
        response = supabase.table("user_restaurante").select("*").eq("id", user_id).execute()
        return response
    
    def get_user_by_email(self, email: str):
        response = supabase.table("user_restaurante").select("*").eq("email", email).execute()
        return response
    
    def get_user_all_restaurante(self):
        response = supabase.table("user_restaurante").select("*").execute()
        return response
    
    def update_user_restaurante(self, user_id: int, user_data: dict):
        response = supabase.table("user_restaurante").update(user_data).eq("id", user_id).execute()
        return response
    
    def delete_user_restaurante(self, user_id: int):
        response = supabase.table("user_restaurante").delete().eq("id", user_id).execute()
        return response

user_restaurante_service = UserRestauranteService()