class ProductDataBlock:    
    def __init__(self, parent_locator):
        self.parent_locator = parent_locator
    
    #region Locators
    TITLE = (".inventory_item_name")
    DESCRIPTION = (".inventory_item_desc")
    PRICE = (".inventory_item_price")
    IMAGE = ("img.inventory_item_img")
    ADD_TO_CART = ("button[id^=add-to-cart]")
    REMOVE_FROM_CART = ("button[id^=remove]")
    #endregion

    def click_add_to_cart_btn(self):
        self.parent_locator.locator(self.ADD_TO_CART).click()
        return self
    
    def click_remove_from_cart_btn(self):
        self.parent_locator.locator(self.REMOVE_FROM_CART).click()
        return self