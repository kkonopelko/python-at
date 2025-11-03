import pytest

from playwright.sync_api import sync_playwright
from utils.browser_manager import *

@pytest.fixture(scope="session", autouse=True)
def browser():
    with sync_playwright() as pw:
        browser = get_browser_type(pw).launch(**get_launch_options()) #driver instance created once, but context and page for each test
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):  
    context = browser.new_context(**get_context_options())
    page = context.new_page()
    yield page
    context.close()