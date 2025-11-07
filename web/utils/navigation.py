from typing import TypeVar, Type
from config.config_manager import config
from pages.cart.cart_page import CartPage
from pages.inventory.inventory_page import InventoryPage
from tests_common.models.enums.relative_uri import RelativeUri

# Generic type for page objects
T = TypeVar('T')

class Navigation:
    def __init__(self, page):
        self.page = page
        self.base_url = config.web_base_url

    def goto(self, relative_url: str):
        self.page.goto(f"{self.base_url}/{relative_url}")
       
    def navigate_to(self, page_class: Type[T], relative_url: str = "") -> T:
        """
        Navigate to a specific page and return an instance of that page.
        
        Args:
            page_class: The page class to instantiate (e.g., CartPage, InventoryPage)
            relative_url: Optional relative URL. If not provided, uses page-specific defaults
            
        Returns:
            Instance of the specified page class
            
        Usage:
            cart_page = navigation.navigate_to(CartPage)
            inventory_page = navigation.navigate_to(InventoryPage, "inventory.html")
        """
        # Use default URLs if not provided
        if not relative_url:
            if page_class == CartPage:
                relative_url = RelativeUri.cart_page.value
            elif page_class == InventoryPage:
                relative_url = RelativeUri.inventory_page.value
        
        full_url = f"{self.base_url}/{relative_url}" if relative_url else self.base_url
        self.page.goto(full_url)
        
        return page_class(self.page)
    
    def refresh_page(self):
        self.page.reload()
        return self
    
    def open_new_tab(self, relative_uri: str = None):
        """Open a new tab and optionally navigate to a URL."""
        context = self.page.context
        new_page = context.new_page()

        if relative_uri:
            if relative_uri.startswith('http'):
                new_page.goto(relative_uri)
            else:
                new_page.goto(f"{self.base_url}/{relative_uri}")

        return new_page
    
    def switch_to_tab(self, tab_index: int):
        """Switch to a specific tab by index.
        
        Args:
            tab_index: Zero-based index of the tab to switch to
            
        Returns:
            The page object of the selected tab
        """
        pages = self.page.context.pages
        if 0 <= tab_index < len(pages):
            target_page = pages[tab_index]
            target_page.bring_to_front()
            return target_page
        else:
            raise IndexError(f"Tab index {tab_index} out of range. Available tabs: {len(pages)}")
    
    def close_current_tab(self):
        self.page.close()
    
    def get_tab_count(self) -> int:
        return len(self.page.context.pages)
    
    def go_back(self):
        self.page.go_back()
        return self
    
    def go_forward(self):
        self.page.go_forward()
        return self