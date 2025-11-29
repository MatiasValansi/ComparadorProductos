from backend.domain.Product import Product

class MercadoLibreMapper:

    @staticmethod
    def to_domain(product_json: dict) -> Product:
        return Product(
            title=product_json.get("title"),
            brand=product_json.get("attributes", [{}])[0].get("value_name") if product_json.get("attributes") else None,
            model=None,  # Se completa cuando definas una lógica para sacar modelo de atributos ML
            price=product_json.get("price", 0),
            provider="mercadolibre",
            provider_id=product_json.get("id"),
            url=product_json.get("permalink")
        )
