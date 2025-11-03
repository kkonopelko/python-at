from config.config_manager import config
class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = config.web_base_url

    def navigate(self, url: str):
        self.page.goto(url)

    def get_current_url(self) -> str:
        return self.page.url