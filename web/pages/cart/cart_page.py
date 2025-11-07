from pages.base_page import BasePage
from pages.cart.cart_item_block import CartItemBlock
from web.models.cart_product_ui_data import CartProductUiData

class CartPage(BasePage):
    #region Locators
    CART_ITEM = ".cart_item"
    #endregion

    def get_products_data(self) -> list[CartProductUiData]:
        cart_items = self.__get_cart_items()
        products_data = []
        
        for cart_item in cart_items:
            product_data = cart_item.get_product_data()
            products_data.append(product_data)
        
        return products_data
    
    def click_on_remove_btn(self, product_title: str):
        self.__find_product_with_title(product_title).click_remove_from_cart_btn()
        return self
    
    def get_cart_items_locator(self):
        return self.page.locator(self.CART_ITEM)

    def __get_cart_items(self) -> list[CartItemBlock]:
        cart_item_locators = self.page.locator(self.CART_ITEM).all()
        return [CartItemBlock(locator) for locator in cart_item_locators]
    
    def __find_product_with_title(self, title: str):
        product_locator = self.page.locator(self.CART_ITEM, has_text=f"{title}")
        return CartItemBlock(product_locator)