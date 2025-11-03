from pages.base_page import BasePage

class MenuSidebar(BasePage):

    #region Locators
    CLOSE_BUTTON = "#react-burger-cross-btn"
    #endregion

    def click_close_button(self):
        return self.page.click(self.CLOSE_BUTTON)