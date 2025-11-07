class ProductDataBlock:    
    def __init__(self, parent_locator):
        self.parent_locator = parent_locator
    
    #region Locators
    TITLE_VALUE = (".inventory_item_name")
    DESCRIPTION_TEXT_VALUE = (".inventory_item_desc")
    PRICE_VALUE = (".inventory_item_price")
    IMAGE = ("img.inventory_item_img")
    ADD_TO_CART_BUTTON = ("button[id^=add-to-cart]")
    REMOVE_FROM_CART_BUTTON = ("button[id^=remove]")
    #endregion

    def click_add_to_cart_btn(self):
        self.parent_locator.locator(self.ADD_TO_CART_BUTTON).click()
        return self
    
    def click_product_title(self):
        self.parent_locator.locator(self.TITLE_VALUE).click()
        return self
    
    def click_remove_from_cart_btn(self):
        self.parent_locator.locator(self.REMOVE_FROM_CART_BUTTON).click()
        return self