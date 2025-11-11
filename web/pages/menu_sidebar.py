from pages.base_page import BasePage

class MenuSidebar(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)

    def click_close_button(self):
        return self.close_btn_locator.click()
    
    def __init_locators__(self, page):
        self.close_btn_locator = page.locator("#react-burger-cross-btn")