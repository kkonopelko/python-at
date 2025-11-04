import re
from playwright.sync_api import Page, expect


class UrlAssertions:
    
    @staticmethod
    def expect_url_contains(page: Page, url_fragment: str):
        pattern = re.compile(rf".*{re.escape(url_fragment)}.*")
        expect(page).to_have_url(pattern)