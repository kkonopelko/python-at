from web.models.cart_product_ui_data import CartProductUiData
from tests_common.models.product_data import ProductData


class ProductMapper:
    
    @staticmethod
    def to_cart_product_ui_model(product: ProductData, quantity: str = "1") -> CartProductUiData:
        return CartProductUiData(
            title=product.title,
            description=product.description,
            price=f"{product.currency}{product.price:.2f}",
            quantity=quantity
        )

    @staticmethod
    def to_cart_product_ui_list(products: list[ProductData], quantity: str = "1") -> list[CartProductUiData]:
        return [ProductMapper.to_cart_product_ui_model(p, quantity) for p in products]