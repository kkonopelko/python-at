import re
from pages.login_page import LoginPage
from playwright.sync_api import expect

class TestLogin:
    
    def test_login_valid_user(self, page):
        #region arrange
        credentials = {
            "username": "standard_user",
            "password": "secret_sauce"
        }
        login_page = LoginPage(page)
        #endregion

        login_page.load()
        inventory_page = login_page.login(credentials["username"], credentials["password"])

        assert inventory_page.get_title() == "Products"
        expect(inventory_page.page).to_have_url(re.compile(r".*inventory\.html$"))  # PLAYWRIGHT ASSERTIONS (Recommended) - Auto-waiting and more reliable
