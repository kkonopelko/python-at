from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#submit"
    SUCCESS_MESSAGE = ".post-title"

    def load(self):
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        self.fill_text(self.USERNAME_INPUT, username)
        self.fill_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_MESSAGE)