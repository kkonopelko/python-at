from pages.base_page import BasePage

class InventoryPage(BasePage):

    #region Locators
    TITLE_TEXT = "[data-test='title']"
    #endregion

    def get_url(self) -> str:
        return self.page.get_url()
    
    def get_title(self) -> str:
        return self.page.inner_text(self.TITLE_TEXT)