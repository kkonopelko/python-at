from pages.base_page import BasePage

class InventoryPage(BasePage):

    #region Locators
    TITLE_TEXT = "[data-test='title']"
    CART_BUTTON = "[data-test='shopping-cart-link']"
    #endregion

    def get_url(self) -> str:
        return self.page.get_url()
    
    def get_title(self) -> str:
        return self.page.inner_text(self.TITLE_TEXT)
    
    def get_cart_button_locator(self):
        return self.page.locator(self.CART_BUTTON)