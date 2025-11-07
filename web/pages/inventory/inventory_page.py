from pages.base_page import BasePage
from pages.inventory.product_data_block import ProductDataBlock
from pages.product_page import ProductPage
from pages.shared.header import Header

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Initialize the base class
        self.header = Header(page)  # Inject Header component

    #region Locators
    TITLE_TEXT = "[data-test='title']"
    PRODUCTS = ".inventory_item"
    #endregion

    def get_url(self) -> str:
        return self.page.get_url()
    
    def get_title(self) -> str:
        return self.page.inner_text(self.TITLE_TEXT)

    def add_product_to_cart(self, product_title: str):
        self.__find_product_with_title(product_title).click_add_to_cart_btn()
        return self
    
    def click_on_product_title(self, title: str):
        self.__find_product_with_title(title).click_product_title()
        return ProductPage(self.page)

    def __find_product_with_title(self, title: str):
        product_locator = self.page.locator(self.PRODUCTS, has_text=f"{title}")
        return ProductDataBlock(product_locator)