from pages.base_page import BasePage
from pages.shared.header import Header

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Initialize the base class
        self.header = Header(page)  # Inject Header component

    #region Locators
    TITLE_TEXT = "[data-test='title']"
    #endregion

    def get_url(self) -> str:
        return self.page.get_url()
    
    def get_title(self) -> str:
        return self.page.inner_text(self.TITLE_TEXT)