import pytest
import random

from playwright.sync_api import expect
from tests.e2e.helpers.shared_steps import login
from tests.e2e.mappers.product_mapper import ProductMapper
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
        inventory_page = login(page, standard_user)
        
        # act
        inventory_page.add_product_to_cart(product.title)

        # assert
        expect(inventory_page.header.get_cart_badge_locator()).to_have_text("1")
        
        cart_page = inventory_page.header.open_cart()
        UrlAssertions.expect_url_contains(cart_page.page, RelativeUri.cart_page.value)
        
        actual_products_in_cart = cart_page.get_products_data()
        assert len(actual_products_in_cart) == 1

        expected_product = ProductMapper.to_cart_product_ui_model(product)
        actual_product = actual_products_in_cart[0]        
        assert actual_product == expected_product

    def test_add_to_cart_multiple_items_from_inventory_page(self, page):
        products = random.sample(all_products, 3)
        inventory_page = login(page, standard_user)
        
        inventory_page.add_product_to_cart(products[0].title) 
        expect(inventory_page.header.get_cart_badge_locator()).to_have_text("1")
        
        inventory_page.add_product_to_cart(products[1].title) 
        expect(inventory_page.header.get_cart_badge_locator()).to_have_text("2")

        inventory_page.add_product_to_cart(products[2].title) 
        expect(inventory_page.header.get_cart_badge_locator()).to_have_text("3")

        cart_page = inventory_page.header.open_cart()
        UrlAssertions.expect_url_contains(cart_page.page, RelativeUri.cart_page.value)
        
        actual_products_in_cart = cart_page.get_products_data()
        assert len(actual_products_in_cart) == 3

        expected_products = ProductMapper.to_cart_product_ui_list(products)     
        assert actual_products_in_cart == expected_products
