class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_text(self, locator: str, text: str):
        self.page.fill(locator, text)

    def click(self, locator: str):
        self.page.click(locator)

    def get_text(self, locator: str) -> str:
        return self.page.inner_text(locator)