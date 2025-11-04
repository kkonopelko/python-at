
from pages.menu_sidebar import MenuSidebar
from pages.cart.cart_page import CartPage

class Header:    
    def __init__(self, page):
        self.page = page
    
    #region Locators
    CART_BUTTON = "[data-test='shopping-cart-link']"
    CART_BADGE = ".shopping_cart_badge"
    MENU_BUTTON = "#react-burger-menu-btn"
    #endregion
    
    def get_cart_button_locator(self):
        return self.page.locator(self.CART_BUTTON)

    def get_menu_button_locator(self):
        return self.page.locator(self.MENU_BUTTON)
    
    def click_menu_button(self):
        self.page.click(self.MENU_BUTTON)
        return MenuSidebar(self.page)
    
    def open_cart(self):
        self.page.click(self.CART_BUTTON)
        return CartPage(self.page)  
    
    def get_cart_badge_locator(self):
        return self.page.locator(self.CART_BADGE)