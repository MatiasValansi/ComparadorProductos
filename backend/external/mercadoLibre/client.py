import httpx

class MercadoLibreClient:
    BASE_URL = "https://api.mercadolibre.com"

    async def search(self, query: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/sites/MLA/search",
                params={"q": query}
            )
            response.raise_for_status()
            return response.json()

    async def get_product(self, product_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}/items/{product_id}")
            response.raise_for_status()
            return response.json()
