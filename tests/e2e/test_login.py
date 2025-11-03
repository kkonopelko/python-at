import re
import pytest

from pages.login_page import LoginPage
from playwright.sync_api import expect
from tests_common.test_data.user_data import *
from tests_common.test_data.ui_text_view_data import *

@pytest.mark.e2e
@pytest.mark.smoke
class TestLogin:
    
    def test_login_valid_user(self, page):
        login_page = LoginPage(page)

        login_page.load()
        inventory_page = login_page.login(standard_user.username, standard_user.password)

        assert inventory_page.get_title() == INVENTORY_PAGE_TITLE_TEXT
        expect(inventory_page.page).to_have_url(re.compile(r".*inventory\.html$"))  # PLAYWRIGHT ASSERTIONS (Recommended) - Auto-waiting and more reliable
        expect(inventory_page.get_cart_button_locator()).to_be_visible()

    def test_login_error_for_required_fields(self, page):        
        login_page = LoginPage(page)

        login_page.load()
        login_page.click_login_btn()

        expect(login_page.get_error_message_locator()).to_have_text(USERNAME_ERROR_MESSAGE)

        login_page.click_error_close_btn()
        login_page.fill_login_credentials(standard_user.username, "")
        login_page.click_login_btn()

        expect(login_page.get_error_message_locator()).to_have_text(PASSWORD_ERROR_MESSAGE)
    
    incorrect_username = UserCredentials(username="incorrect_username", password=standard_user.password)
    incorrect_password = UserCredentials(username=standard_user.username, password="incorrect_password")

    @pytest.mark.parametrize("credentials", 
                             [incorrect_username, incorrect_password],
                             ids=["incorrect_username", "incorrect_password"])
    def test_login_error_for_incorrect_user_credentials(self, page, credentials):
        login_page = LoginPage(page)

        login_page.load()
        login_page.fill_login_credentials(credentials.username, credentials.password)
        login_page.click_login_btn()

        expect(login_page.get_error_message_locator()).to_have_text(USERNAME_AND_PASSWORD_DONOT_MATCH_ERROR_MESSAGE)

    def test_login_error_for_locked_out_user(self, page):
        login_page = LoginPage(page)

        login_page.load()
        login_page.fill_login_credentials(locked_out_user.username, locked_out_user.password)
        login_page.click_login_btn()

        expect(login_page.get_error_message_locator()).to_have_text(USER_LOCKED_OUT_ERROR_MESSAGE)