import os
from typing import Any, Dict

import httpx


class MercadoLibreClient:
    BASE_URL = "https://api.mercadolibre.com"

    def _default_headers(self) -> Dict[str, str]:
        """Headers necesarios para evitar bloqueos (403) de la API pública.

        Si existe la variable de entorno `MERCADOLIBRE_ACCESS_TOKEN`, se envía
        también el header `Authorization: Bearer <token>` para usar la API
        autenticada oficial de Mercado Libre.
        """

        headers: Dict[str, str] = {
            # User-Agent de navegador moderno para evitar bloqueos por "bot".
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            # Según la documentación oficial, la API responde JSON.
            "Accept": "application/json",
            "Accept-Language": "es-AR,es;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
        }

        access_token = os.getenv("MERCADOLIBRE_ACCESS_TOKEN")
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"

        return headers

    async def search(self, query: str) -> Dict[str, Any]:
        """Consulta el endpoint oficial de búsqueda de Mercado Libre y devuelve el JSON crudo.

        Lanza una excepción clara si Mercado Libre responde con 403.
        """

        async with httpx.AsyncClient(headers=self._default_headers(), timeout=10.0) as client:
            response = await client.get(
                f"{self.BASE_URL}/sites/MLA/search",
                params={"q": query},
            )

            if response.status_code == 403:
                # Incluir parte del cuerpo para ayudar a diagnosticar el motivo
                body = response.text[:300]
                raise PermissionError(
                    "Mercado Libre devolvió 403 Forbidden al buscar productos. "
                    "Revisa los headers enviados (User-Agent, Accept, Accept-Language, Authorization) "
                    "y los límites de uso de la API pública. Detalle: " + body
                )

            response.raise_for_status()
            return response.json()

    async def get_product(self, product_id: str) -> Dict[str, Any]:
        """Obtiene el detalle de un producto individual por ID en Mercado Libre."""

        async with httpx.AsyncClient(headers=self._default_headers(), timeout=10.0) as client:
            response = await client.get(f"{self.BASE_URL}/items/{product_id}")

            if response.status_code == 403:
                body = response.text[:300]
                raise PermissionError(
                    "Mercado Libre devolvió 403 Forbidden al obtener el producto. "
                    "Revisa los headers enviados (User-Agent, Accept, Accept-Language, Authorization) "
                    "y los límites de uso de la API pública. Detalle: " + body
                )

            response.raise_for_status()
            return response.json()
