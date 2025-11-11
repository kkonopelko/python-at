
from pages.base_page import BasePage
from pages.checkout.checkout_complete_page import CheckoutCompletePage
from pages.shared.header import Header

class CheckoutOverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)
        self.header = Header(page)

    def click_finish_button(self):
        self.finish_btn_locator.click()
        return CheckoutCompletePage(self.page)

    def __init_locators__(self, page):
        self.finish_btn_locator = page.locator("#finish")