from web.models.cart_product_ui_data import CartProductUiData

class CartItemBlock:
    def __init__(self, parent_locator):
        self.parent_locator = parent_locator

    #region Locators (relative to the cart item)
    TITLE = ".inventory_item_name"
    QUANTITY = ".cart_quantity"
    DESCRIPTION = ".inventory_item_desc"
    PRICE = ".inventory_item_price"
    REMOVE = ".cart_button"
    #endregion

    def get_product_data(self) -> CartProductUiData:
        return CartProductUiData(
            title=self.parent_locator.locator(self.TITLE).inner_text(),
            quantity=self.parent_locator.locator(self.QUANTITY).inner_text(),
            description=self.parent_locator.locator(self.DESCRIPTION).inner_text(),
            price=self.parent_locator.locator(self.PRICE).inner_text()
        )
