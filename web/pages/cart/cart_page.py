from pages.base_page import BasePage
from pages.cart.cart_item_block import CartItemBlock
from pages.checkout.checkout_information_page import CheckoutInformationPage
from web.models.cart_product_ui_data import CartProductUiData

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)

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
        return self.cart_items_locator
    
    def click_checkout(self):
        self.checkout_button_locator.click()
        return CheckoutInformationPage(self.page)

    def __get_cart_items(self) -> list[CartItemBlock]:
        cart_item_locators = self.cart_items_locator.all()
        return [CartItemBlock(locator) for locator in cart_item_locators]
    
    def __find_product_with_title(self, title: str):
        product_locator = self.cart_item_by_title_locator(title)
        return CartItemBlock(product_locator)
    
    def __init_locators__(self, page):
        self.cart_items_locator = page.locator(".cart_item")
        self.cart_item_by_title_locator = lambda title: page.locator(".cart_item", has_text=f"{title}")
        self.checkout_button_locator = page.locator("#checkout")