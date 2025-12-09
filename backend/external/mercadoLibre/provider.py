from typing import List

from backend.external.provider_interface import ProductProvider
from .client import MercadoLibreClient
from .mapper import MercadoLibreMapper
from backend.domain.Product import Product


class MercadoLibreProvider(ProductProvider):

    def __init__(self) -> None:
        self.client = MercadoLibreClient()

    async def search(self, query: str) -> List[Product]:
        """Busca productos en Mercado Libre y los normaliza al dominio `Product`."""

        raw = await self.client.search(query)
        results = raw.get("results", [])
        return [MercadoLibreMapper.to_domain(item) for item in results]

    async def get_product(self, product_id: str) -> Product:
        """Obtiene un único producto de Mercado Libre por ID y lo mapea a `Product`."""

        raw = await self.client.get_product(product_id)
        return MercadoLibreMapper.to_domain(raw)
