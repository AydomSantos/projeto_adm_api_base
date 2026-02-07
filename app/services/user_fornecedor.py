from app.core.supabase import supabase

class UserFornecedorService:
    def create_user_fornecedor(self, user_data: dict):
        response = supabase.table("user_fornecedor").insert(user_data).execute()
        return response
    
    def get_user_fornecedor_by_id(self, user_id: int):
        response = supabase.table("user_fornecedor").select("*").eq("id", user_id).execute()
        return response
    
    def get_user_by_email(self, email: str):
        response = supabase.table("user_fornecedor").select("*").eq("email", email).execute()
        return response
    
    def get_user_all_fornecedor(self):
        response = supabase.table("user_fornecedor").select("*").execute()
        return response
    
    def update_user_fornecedor(self, user_id: int, user_data: dict):
        response = supabase.table("user_fornecedor").update(user_data).eq("id", user_id).execute()
        return response
    
    def delete_user_fornecedor(self, user_id: int):
        response = supabase.table("user_fornecedor").delete().eq("id", user_id).execute()
        return response

user_fornecedor_service = UserFornecedorService()