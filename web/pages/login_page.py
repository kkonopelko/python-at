from pages.base_page import BasePage
from pages.inventory.inventory_page import InventoryPage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)

    def load(self):
        self.navigate(self.base_url)
        return self

    def login(self, username: str, password: str):
        self.username_input_locator.fill(username)
        self.password_input_locator.fill(password)
        self.login_button_locator.click()
        return InventoryPage(self.page)
    
    def fill_login_credentials(self, username: str, password: str):
        self.username_input_locator.fill(username)
        self.password_input_locator.fill(password)
        return self
    
    def click_login_btn(self):
        self.login_button_locator.click()

    def click_error_close_btn(self):
        self.error_close_button_locator.click()
        return self

    def get_error_message(self) -> str:
        return self.error_message_locator.inner_text()

    def get_error_message_locator(self):
        return self.error_message_locator

    def __init_locators__(self, page):
        self.username_input_locator = page.locator("[data-test='username']")
        self.password_input_locator = page.locator("[data-test='password']")
        self.login_button_locator = page.locator("[data-test='login-button']")
        self.error_message_locator = page.locator("[data-test='error']")
        self.error_close_button_locator = page.locator("[data-test='error-button']")