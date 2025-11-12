
from pages.base_page import BasePage
from pages.checkout.checkout_overview_page import CheckoutOverviewPage
from pages.shared.header import Header

class CheckoutInformationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__init_locators__(page)
        self.header = Header(page)

    def fill_first_name(self, first_name: str):
        self.first_name_input_locator.fill(first_name)
        return self

    def fill_last_name(self, last_name: str):   
        self.last_name_input_locator.fill(last_name)
        return self 

    def fill_zip_code(self, zip_code: str):  
        self.zip_code_input_locator.fill(zip_code)
        return self

    def fill_checkout_information(self, first_name: str, last_name: str, zip_code: str):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_zip_code(zip_code)
        return self
    
    def click_continue_button(self):
        self.continue_button_locator.click()
        return CheckoutOverviewPage(self.page)
    
    def get_error_message_text_locator(self):
        return self.error_message_locator
    
    def get_error_message_text(self) -> str:
        return self.error_message_locator.inner_text().strip()
    
    def click_close_error_button(self):
        self.error_btn_locator.click()
        return self

    def __init_locators__(self, page):
        self.first_name_input_locator = page.locator("#first-name")
        self.last_name_input_locator = page.locator("#last-name")
        self.zip_code_input_locator = page.locator("#postal-code")
        self.continue_button_locator = page.locator("#continue")
        self.error_message_locator = page.locator("[data-test='error']")
        self.error_btn_locator = page.locator(".error-button")