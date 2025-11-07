from web.models.cart_product_ui_data import CartProductUiData

class CartItemBlock:
    def __init__(self, parent_locator):
        self.parent_locator = parent_locator

    #region Locators (relative to the cart item)
    TITLE_TEXT_VALUE = ".inventory_item_name"
    QUANTITY = ".cart_quantity"
    DESCRIPTION_TEXT_VALUE = ".inventory_item_desc"
    PRICE_VALUE = ".inventory_item_price"
    REMOVE_BUTTON = ".cart_button"
    #endregion

    def get_product_data(self) -> CartProductUiData:
        return CartProductUiData(
            title=self.parent_locator.locator(self.TITLE_TEXT_VALUE).inner_text().strip(),
            quantity=self.parent_locator.locator(self.QUANTITY).inner_text().strip(),
            description=self.parent_locator.locator(self.DESCRIPTION_TEXT_VALUE).inner_text().strip(),
            price=self.parent_locator.locator(self.PRICE_VALUE).inner_text().strip()
        )
