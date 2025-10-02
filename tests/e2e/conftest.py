import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True for CI
        context = browser.new_context()
        yield context
        context.close()
        browser.close()