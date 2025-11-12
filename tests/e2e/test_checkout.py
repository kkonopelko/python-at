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

        assert checkout_overview_page.get_payment_information_value() == PAYMENT_INFORMATION_TEXT
        assert checkout_overview_page.get_shipping_information_value() == SHIPPING_INFORMATION_TEXT
        assert checkout_overview_page.get_item_total_value() == ITEM_TOTAL_TEXT(product.price)
        assert checkout_overview_page.get_tax_value() == TAX_TEXT(self.__calculate_tax__(product.price))
        assert checkout_overview_page.get_total_value() == TOTAL(product.price, self.__calculate_tax__(product.price))

        checkout_complete_page = checkout_overview_page.click_finish_button()
        UrlAssertions.expect_url_contains(checkout_complete_page.page, RelativeUri.checkout_complete_page.value)
        expect(checkout_complete_page.get_back_to_products_btn_locator()).to_be_visible()
        assert checkout_complete_page.get_complete_header_text() == CHECKOUT_COMPLETE_HEADER_TEXT
        assert checkout_complete_page.get_complete_text() == CHECKOUT_COMPLETE_TEXT

        checkout_complete_page.header.open_cart()
        expect(cart_page.get_cart_items_locator()).not_to_be_visible()

    def test_checkout_with_multiple_items(self, page):
        products = random.sample(all_products, 2)
        total_price = sum(product.price for product in products)
        total_tax = self.__calculate_tax__(total_price)

        inventory_page = login(page, standard_user)
        inventory_page.add_product_to_cart(products[0].title)
        inventory_page.add_product_to_cart(products[1].title)
        cart_page = inventory_page.header.open_cart()

        checkout_information_page = cart_page.click_checkout()
        UrlAssertions.expect_url_contains(checkout_information_page.page, RelativeUri.checkout_step_one_page.value)

        checkout_information_page.fill_checkout_information("TestFirstName", "TestLastName", "12345")
        checkout_overview_page = checkout_information_page.click_continue_button()
        UrlAssertions.expect_url_contains(checkout_overview_page.page, RelativeUri.checkout_step_two_page.value)

        assert checkout_overview_page.get_payment_information_value() == PAYMENT_INFORMATION_TEXT
        assert checkout_overview_page.get_shipping_information_value() == SHIPPING_INFORMATION_TEXT
        assert checkout_overview_page.get_item_total_value() == ITEM_TOTAL_TEXT(total_price)
        assert checkout_overview_page.get_tax_value() == TAX_TEXT(total_tax)
        assert checkout_overview_page.get_total_value() == TOTAL(total_price, total_tax)

        checkout_complete_page = checkout_overview_page.click_finish_button()
        UrlAssertions.expect_url_contains(checkout_complete_page.page, RelativeUri.checkout_complete_page.value)
        expect(checkout_complete_page.get_back_to_products_btn_locator()).to_be_visible()
        assert checkout_complete_page.get_complete_header_text() == CHECKOUT_COMPLETE_HEADER_TEXT
        assert checkout_complete_page.get_complete_text() == CHECKOUT_COMPLETE_TEXT

        checkout_complete_page.header.open_cart()
        expect(cart_page.get_cart_items_locator()).not_to_be_visible()

    def test_checkout_shipping_information_fields_are_required(self, page):
        product = random.choice(all_products)
        inventory_page = login(page, standard_user)

        inventory_page.add_product_to_cart(product.title)
        cart_page = inventory_page.header.open_cart()

        checkout_information_page = cart_page.click_checkout()        
        checkout_information_page.click_continue_button()
        assert checkout_information_page.get_error_message_text() == FIRST_NAME_ERROR_MESSAGE

        checkout_information_page.fill_first_name("TestFirstName")
        checkout_information_page.click_continue_button()
        assert checkout_information_page.get_error_message_text() == LAST_NAME_ERROR_MESSAGE

        checkout_information_page.fill_last_name("TestLastName")
        checkout_information_page.click_continue_button()
        assert checkout_information_page.get_error_message_text() == POSTAL_CODE_ERROR_MESSAGE

        checkout_information_page.click_close_error_button()
        expect(checkout_information_page.get_error_message_text_locator()).not_to_be_visible()

        checkout_information_page.fill_zip_code("12345")
        checkout_overview_page = checkout_information_page.click_continue_button()
        UrlAssertions.expect_url_contains(checkout_overview_page.page, RelativeUri.checkout_step_two_page.value)

    def __calculate_tax__(self, product_price) -> float:
        calculated_tax = round(product_price * 0.08, 2)
        return calculated_tax