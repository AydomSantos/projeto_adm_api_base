from fastapi import APIRouter, HTTPException
from app.services.produto_service import produto_service
from app.schemas.produto import ProdutoCreateSchema, ProdutoSchema

router = APIRouter()

@router.post("/", response_model=ProdutoSchema, status_code=201)
async def create_produto(produto: ProdutoCreateSchema):
    response = produto_service.create_produto(produto.model_dump(mode="json"))
    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao criar produto")
    return response.data[0]

@router.get("/{produto_id}", response_model=ProdutoSchema)
async def get_produto(produto_id: int):
    response = produto_service.get_produto_by_id(produto_id)
    if not response.data:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return response.data[0]

@router.put("/{produto_id}", response_model=ProdutoSchema)
async def update_produto(produto_id: int, produto: ProdutoCreateSchema):
    response = produto_service.update_produto(produto_id, produto.model_dump(mode="json"))
    if not response.data:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return response.data[0]

@router.delete("/{produto_id}")
async def delete_produto(produto_id: int):
    response = produto_service.delete_produto(produto_id)
    if not response.data:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}