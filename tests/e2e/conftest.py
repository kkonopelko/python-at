import pytest

from playwright.sync_api import sync_playwright
from config.config_manager import config

@pytest.fixture(scope="session", autouse=True)
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=config.headless_mode)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page(ignore_https_errors=True)
    yield page
    context.close()



