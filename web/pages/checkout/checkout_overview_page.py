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
    
    def get_payment_information_value(self) -> str:
        return self.payment_information_value_locator.inner_text().strip()

    def get_shipping_information_value(self) -> str:
        return self.shipping_information_value_locator.inner_text().strip()
    
    def get_item_total_value(self) -> str:
        return self.item_total_value_locator.inner_text().strip()
    
    def get_tax_value(self) -> str:
        return self.tax_value_locator.inner_text().strip()
    
    def get_total_value(self) -> str:
        return self.total_value_locator.inner_text().strip()

    def __init_locators__(self, page):
        self.finish_btn_locator = page.locator("#finish")
        self.payment_information_value_locator = page.locator("[data-test='payment-info-value']")
        self.shipping_information_value_locator = page.locator("[data-test='shipping-info-value']")
        self.item_total_value_locator = page.locator("[data-test='subtotal-label']")
        self.tax_value_locator = page.locator("[data-test='tax-label']")
        self.total_value_locator = page.locator("[data-test='total-label']")