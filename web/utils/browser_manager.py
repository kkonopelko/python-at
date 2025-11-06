from playwright.sync_api import Playwright, BrowserType
from config.config_manager import config

def get_browser_type(playwright: Playwright) -> BrowserType:
        browser = config.browser_type

        if browser == 'chromium':
            return playwright.chromium

        elif browser == 'firefox':
            return playwright.firefox

        elif browser == 'webkit':
            return playwright.webkit
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
def get_launch_options():
        launch_options = {
            "headless": config.headless_mode,
            "args": ["--start-maximized", "--window-size=1800,720"], # for non-headless mode, doesn't work
            "slow_mo": config.slow_motion
        }
        return launch_options

def get_context_options():        
        if config.headless_mode:
            context_options = {
                "viewport": {"width": 1920, "height": 1080} # for headless mode
            }
            return context_options
        else:
            context_options = {
                "viewport": None  # important! disable fixed viewport
            }
        return context_options