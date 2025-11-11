class ProductDataBlock:    
    def __init__(self, parent_locator):
        self.parent_locator = parent_locator
        self.__init_locators__(parent_locator)

    def click_add_to_cart_btn(self):
        self.add_to_cart_button_locator.click()
        return self
    
    def click_product_title(self):
        self.title_value_locator.click()
        return self
    
    def click_remove_from_cart_btn(self):
        self.remove_from_cart_button_locator.click()
        return self
    
    def __init_locators__(self, parent_locator):
        self.title_value_locator = parent_locator.locator(".inventory_item_name")
        self.description_text_value_locator = parent_locator.locator(".inventory_item_desc")
        self.price_value_locator = parent_locator.locator(".inventory_item_price")
        self.image_locator = parent_locator.locator("img.inventory_item_img")
        self.add_to_cart_button_locator = parent_locator.locator("button[id^=add-to-cart]")
        self.remove_from_cart_button_locator = parent_locator.locator("button[id^=remove]")