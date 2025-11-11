from pages.base_page import BasePage
from pages.inventory.product_data_block import ProductDataBlock
from pages.product_page import ProductPage
from pages.shared.header import Header

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)
        self.header = Header(page)  # Inject Header component

    def get_url(self) -> str:
        return self.page.get_url()
    
    def get_title(self) -> str:
        return self.title_text_locator.inner_text()

    def add_product_to_cart(self, product_title: str):
        self.__find_product_with_title(product_title).click_add_to_cart_btn()
        return self
    
    def remove_product_from_cart(self, product_title: str):
        self.__find_product_with_title(product_title).click_remove_from_cart_btn()
        return self
    
    def click_on_product_title(self, title: str):
        self.__find_product_with_title(title).click_product_title()
        return ProductPage(self.page)

    def __find_product_with_title(self, title: str):
        return ProductDataBlock(self.product_by_title_locator(title))
    
    def __init_locators__(self, page):
        self.title_text_locator = page.locator("[data-test='title']")
        self.product_by_title_locator = lambda title: page.locator(".inventory_item", has_text=f"{title}")