from pages.base_page import BasePage
from pages.shared.header import Header

class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)
        self.header = Header(page)

    def get_complete_header_text(self) -> str:
        return self.complete_header_locator.inner_text().strip()
    
    def get_complete_text(self) -> str:
        return self.complete_text_locator.inner_text().strip()
    
    def get_back_to_products_btn_locator(self):
        return self.back_to_products_btn_locator

    def __init_locators__(self, page):
        self.complete_header_locator = page.locator(".complete-header")
        self.complete_text_locator = page.locator(".complete-text")
        self.back_to_products_btn_locator = page.locator("#back-to-products")