
from pages.inventory.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests_common.models.user_credentials import UserCredentials

def login(page, userCredentials: UserCredentials) -> InventoryPage:
    login_page = LoginPage(page)
    login_page.load()
    return login_page.login(userCredentials.username, userCredentials.password)