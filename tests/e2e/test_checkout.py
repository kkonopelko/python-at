import pytest
import random

from playwright.sync_api import expect
from tests.e2e.helpers.shared_steps import login
from tests_common.models.enums.relative_uri import RelativeUri
from tests_common.test_data.products_data_provider import *
from tests_common.test_data.users_data_provider import *
from tests_common.constants.ui_text_view_data import *
from tests.e2e.helpers.url_assertions import UrlAssertions

@pytest.mark.e2e
@pytest.mark.regression
class TestCheckout:
    
    def test_checkout_with_single_item(self, page):
        product = random.choice(all_products)        
        inventory_page = login(page, standard_user)

        inventory_page.add_product_to_cart(product.title)
        cart_page = inventory_page.header.open_cart()

        checkout_information_page = cart_page.click_checkout()
        UrlAssertions.expect_url_contains(checkout_information_page.page, RelativeUri.checkout_step_one_page.value)

        checkout_information_page.fill_checkout_information("TestFirstName", "TestLastName", "12345")
        checkout_overview_page = checkout_information_page.click_continue_button()
        UrlAssertions.expect_url_contains(checkout_overview_page.page, RelativeUri.checkout_step_two_page.value)
        
        # check data

        checkout_complete_page = checkout_overview_page.click_finish_button()
        UrlAssertions.expect_url_contains(checkout_complete_page.page, RelativeUri.checkout_complete_page.value)
        expect(checkout_complete_page.get_back_to_products_btn_locator()).to_be_visible()
        assert checkout_complete_page.get_complete_header_text() == CHECKOUT_COMPLETE_HEADER_TEXT
        assert checkout_complete_page.get_complete_text() == CHECKOUT_COMPLETE_TEXT

        checkout_complete_page.header.open_cart()
        expect(cart_page.get_cart_items_locator()).not_to_be_visible()