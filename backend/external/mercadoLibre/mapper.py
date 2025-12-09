from typing import Any, Dict

from backend.domain.Product import Product


class MercadoLibreMapper:

    @staticmethod
    def to_domain(product_json: Dict[str, Any]) -> Product:
        """Mapea un ítem crudo de la API de Mercado Libre al dominio `Product`.

        Cada producto de dominio resultante expone al menos:
        - title
        - price
        - image_url (a partir de `thumbnail` o `secure_thumbnail`)
        - url (permalink oficial del producto)
        - provider = "mercadolibre"
        """

        attributes = product_json.get("attributes") or []
        brand = None
        if attributes and isinstance(attributes, list):
            # Heurística simple: tomar el primer atributo que tenga value_name como marca.
            first_attr = attributes[0] or {}
            brand = first_attr.get("value_name")

        image_url = (
            product_json.get("secure_thumbnail")
            or product_json.get("thumbnail")
        )

        return Product(
            title=product_json.get("title", ""),
            brand=brand,
            model=None,  # Se puede completar más adelante a partir de otros atributos.
            price=float(product_json.get("price", 0.0)),
            provider="mercadolibre",
            provider_id=product_json.get("id", ""),
            url=product_json.get("permalink", ""),
            image_url=image_url,
        )
