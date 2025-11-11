
from pages.menu_sidebar import MenuSidebar
from pages.cart.cart_page import CartPage

class Header:    
    def __init__(self, page):
        self.page = page
        self.__init_locators__(page)  
    
    def click_menu_button(self):
        self.menu_btn_locator.click()
        return MenuSidebar(self.page)
    
    def open_cart(self):
        self.cart_btn_locator.click()
        return CartPage(self.page)  
    
    def get_cart_badge_locator(self):
        return self.cart_badge_locator
    
    def get_cart_button_locator(self):
        return self.cart_btn_locator

    def get_menu_button_locator(self):
        return self.menu_btn_locator
    
    def __init_locators__(self, page):
        self.cart_btn_locator = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge_locator = page.locator(".shopping_cart_badge")
        self.menu_btn_locator = page.locator("#react-burger-menu-btn")