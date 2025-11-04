from config.config_manager import config

class Navigation:
    def __init__(self, page):
        self.page = page
        self.base_url = config.web_base_url

    def goto(self, relative_url: str):
        self.page.goto(f"{self.base_url}/{relative_url}")
    
    def refresh_page(self):
        self.page.reload()
        return self
    
    def open_new_tab(self, url: str = None):
        """Open a new tab and optionally navigate to a URL.
        
        Args:
            url: Optional URL to navigate to in the new tab
            
        Returns:
            The new page object for the opened tab
        """
        # Get the browser context from the current page
        context = self.page.context
        
        # Create new page (tab)
        new_page = context.new_page()
        
        # Navigate to URL if provided
        if url:
            if url.startswith('http'):
                new_page.goto(url)
            else:
                # Treat as relative URL
                new_page.goto(f"{self.base_url}/{url}")
        
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