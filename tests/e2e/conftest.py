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
def page(browser, request):
    context = browser.new_context(**get_context_options())

    test_name = request.node.name
    start_trace_record(context, test_name)

    page = context.new_page()
    yield page

    capture_screenshot_on_failure(page, request, test_name)
    save_trace_record_on_failure(context, request, test_name)
    context.close()

def start_trace_record(context, test_name: str):
    context.tracing.start(title=test_name, screenshots=True, snapshots=True, sources=True)

def save_trace_record_on_failure(context, request, test_name: str):
    if request.node.rep_call.failed:
        trace_path = f"{config.debug_artefacts_directory}/failed_{test_name}/trace_{test_name}.zip"
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()

def capture_screenshot_on_failure(page, request, test_name: str):
    if request.node.rep_call.failed:
        screenshot_path = f"{config.debug_artefacts_directory}/failed_{test_name}/screenshot_{test_name}.png"
        page.screenshot(path=screenshot_path)