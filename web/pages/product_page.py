from pages.base_page import BasePage
from pages.shared.header import Header

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)

    #region Locators
    ADD_TO_CART_BUTTON = "#add-to-cart"
    BACK_TO_PRODUCTS_BUTTON = "#back-to-products"
    REMOVE_BUTTON= "#remove"
    #endregion

    def click_add_to_cart_btn(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).click()
        return self
    
    def click_remove_btn(self):
        self.page.locator(self.REMOVE_BUTTON).click()
        return self

    def click_back_to_products_btn(self):
        self.page.locator(self.BACK_TO_PRODUCTS_BUTTON).click()
        return self