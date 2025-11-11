from pages.base_page import BasePage
from pages.shared.header import Header

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)
        self.header = Header(page)

    def click_add_to_cart_btn(self):
        self.add_to_cart_btn_locator.click()
        return self
    
    def click_remove_btn(self):
        self.remove_btn_locator.click()
        return self

    def click_back_to_products_btn(self):
        self.back_to_products_btn_locator.click()
        return self
    
    def __init_locators__(self, page):
        self.add_to_cart_btn_locator = page.locator("#add-to-cart")
        self.back_to_products_btn_locator = page.locator("#back-to-products")
        self.remove_btn_locator = page.locator("#remove")