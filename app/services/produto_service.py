from app.core.supabase import supabase

class ProdutoService:
    def create_produto(self, produto_data: dict):
        response = supabase.table("produtos").insert(produto_data).execute()
        return response
    
    def get_produto_by_id(self, produto_id: int):
        response = supabase.table("produtos").select("*").eq("id", produto_id).execute()
        return response
    
    def get_all_produtos(self):
        response = supabase.table("produtos").select("*").execute()
        return response
    
    def update_produto(self, produto_id: int, produto_data: dict):
        response = supabase.table("produtos").update(produto_data).eq("id", produto_id).execute()
        return response
    
    def delete_produto(self, produto_id: int):
        response = supabase.table("produtos").delete().eq("id", produto_id).execute()
        return response

produto_service = ProdutoService()