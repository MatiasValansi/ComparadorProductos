from fastapi import APIRouter
from backend.service.product_search_service import ProductSearchService
from backend.external.mercadoLibre.provider import MercadoLibreProvider

router = APIRouter(prefix="/products", tags=["products"])

provider = MercadoLibreProvider()
service = ProductSearchService(provider)

@router.get("/search")
async def search_products(q: str):
    return await service.search_products(q)
    