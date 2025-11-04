import pytest
import random

from pages.login_page import LoginPage
from playwright.sync_api import expect
from tests_common.models.enums.relative_uri import RelativeUri
from tests_common.test_data.products_data_provider import *
from tests_common.test_data.users_data_provider import *
from tests_common.constants.ui_text_view_data import *
from tests.e2e.helpers.url_assertions import UrlAssertions

@pytest.mark.e2e
@pytest.mark.regression
class TestCart:
    
    def test_add_to_cart_single_item_from_inventory_page(self, page):
        # arrange
        product = random.choice(all_products)
        
        login_page = LoginPage(page)
        login_page.load()
        inventory_page = login_page.login(standard_user.username, standard_user.password)
        
        # act
        inventory_page.add_product_to_cart(product.title)

        # assert
        expect(inventory_page.header.get_cart_badge_locator()).to_have_text("1")
        
        cart_page = inventory_page.header.open_cart()
        UrlAssertions.expect_url_contains(cart_page.page, RelativeUri.cart_page.value)
        
        actual_products_in_cart = cart_page.get_products_data()
        assert len(actual_products_in_cart) == 1

        actual_product = actual_products_in_cart[0]
        assert actual_product.title == product.title
        assert actual_product.description == product.description
