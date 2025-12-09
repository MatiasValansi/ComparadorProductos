from typing import List, Dict, Any

from fastapi import APIRouter, HTTPException

from backend.domain.Product import Product
from backend.service.product_search_service import ProductSearchService
from backend.external.mercadoLibre.provider import MercadoLibreProvider


router = APIRouter(prefix="/products", tags=["products"])


# En el futuro se pueden agregar más proveedores (AmazonProvider, etc.).
providers = [MercadoLibreProvider()]
service = ProductSearchService(providers)


def _to_response_dto(product: Product) -> Dict[str, Any]:
    """Normaliza el modelo de dominio `Product` al JSON expuesto al frontend.

    Estructura de salida por producto:
    - title
    - price
    - image
    - permalink
    - source
    """

    return {
        "title": product.title,
        "price": product.price,
        "image": product.image_url,
        "permalink": product.url,
        "source": product.provider,
    }


@router.get("/search")
async def search_products(q: str) -> List[Dict[str, Any]]:
    """Endpoint de búsqueda unificada de productos.

    GET /api/products/search?q=Notebook
    """

    try:
        products = await service.search_products(q)
    except PermissionError as exc:
        # Error específico de acceso a la API de Mercado Libre.
        raise HTTPException(status_code=502, detail=str(exc))

    return [_to_response_dto(p) for p in products]
    