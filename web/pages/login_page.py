from pages.base_page import BasePage
from pages.inventory.inventory_page import InventoryPage

class LoginPage(BasePage):

    #region Locators
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"
    ERROR_CLOSE_BUTTON = "[data-test='error-button']"
    #endregion

    def load(self):
        self.navigate(self.base_url)
        return self

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
        return InventoryPage(self.page)
    
    def fill_login_credentials(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        return self
    
    def click_login_btn(self):
        self.page.click(self.LOGIN_BUTTON)

    def click_error_close_btn(self):
        self.page.click(self.ERROR_CLOSE_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.page.inner_text(self.ERROR_MESSAGE)
    
    def get_error_message_locator(self):
        return self.page.locator(self.ERROR_MESSAGE)