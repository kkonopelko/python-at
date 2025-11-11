from web.models.cart_product_ui_data import CartProductUiData

class CartItemBlock:
    def __init__(self, parent_locator):
        self.parent_locator = parent_locator
        self.__init_locators__(parent_locator)

    def get_product_data(self) -> CartProductUiData:
        return CartProductUiData(
            title=self.title_text_value_locator.inner_text().strip(),
            quantity=self.quantity_locator.inner_text().strip(),
            description=self.description_text_value_locator.inner_text().strip(),
            price=self.price_value_locator.inner_text().strip()
        )

    def click_remove_from_cart_btn(self):
        self.remove_button_locator.click()
        return self

    def __init_locators__(self, parent_locator):  # relative to the cart item
        self.title_text_value_locator = parent_locator.locator(".inventory_item_name")
        self.quantity_locator = parent_locator.locator(".cart_quantity")
        self.description_text_value_locator = parent_locator.locator(".inventory_item_desc")
        self.price_value_locator = parent_locator.locator(".inventory_item_price")
        self.remove_button_locator = parent_locator.locator("button[id^=remove]")