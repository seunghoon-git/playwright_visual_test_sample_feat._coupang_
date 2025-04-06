import pytest
from playwright.sync_api import sync_playwright
import time
import os


pytest.login_page_url = "https://login.coupang.com/login/login.pang"
pytest.coupang_home_url = "https://www.coupang.com/"
pytest.coupang_mobile_web_home_url = "https://m.coupang.com/"

@pytest.fixture(scope = 'session')
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

##### set up web browsers #####
@pytest.fixture(scope="session")
def web_browser(playwright_instance, request):
    if request.config.getoption("--browser"):
        browser_type = request.config.getoptin("--browser")[0]
    else:
        browser_type = "chromium"

    headed = request.config.getoption("--headed")

    browser = getattr(playwright_instance, browser_type).launch(headless = not headed)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def setup_web_browser(web_browser, request):
    trace_option = request.config.getoption("--tracing")

    context = web_browser.new_context(
        viewport = {"width": 1470, "height": 750},
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    if trace_option == 'on':
        trace_name = request.node.name
        trace_dir = "test-results"
        os.makedirs(trace_dir, exist_ok = True)
        trace_path = os.path.join(trace_dir, f"trace-{trace_name}.zip")
        context.tracing.stop(path=trace_path)
    else:
        if request.node.rep_call.failed:
            test_name = request.node.name
            trace_dir = "test-results"
            os.makedirs(trace_dir, exist_ok=True)
            trace_path = os.path.join(trace_dir, f"trace-{test_name}.zip")
            context.tracing.stop(path=trace_path)
        else:
            context.tracing.stop()

    context.close()


@pytest.fixture(scope="function")
def setup_web_browser_popup(web_browser, request):
    trace_option = request.config.getoption("--tracing")

    context = web_browser.new_context(
        viewport = {"width": 400, "height": 639},
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    if trace_option == 'on':
        trace_name = request.node.name
        trace_dir = "test-results"
        os.makedirs(trace_dir, exist_ok = True)
        trace_path = os.path.join(trace_dir, f"trace-{trace_name}.zip")
        context.tracing.stop(path=trace_path)
    else:
        if request.node.rep_call.failed:
            test_name = request.node.name
            trace_dir = "test-results"
            os.makedirs(trace_dir, exist_ok=True)
            trace_path = os.path.join(trace_dir, f"trace-{test_name}.zip")
            context.tracing.stop(path=trace_path)
        else:
            context.tracing.stop()

    context.close()
#################################


######## set up mobile web browsers #######
@pytest.fixture(scope="session")
def mobile_web_brwoser(playwright_instance, request):
    headed = request.config.getoption("--headed")
    galaxy_24 = playwright_instance.devices["Galaxy S24"]
    browser = playwright_instance.webkit.launch(headless = not headed)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def mobile_web_context(mobile_web_browser, playwright_instance, request):
    trace_option = request.config.getoption("--tracing")

    galaxy_24 = playwright_instance.devices["Galaxy S24"]
    context = mobile_web_browser.new_context(**galaxy_24)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context

    if trace_option == 'on':
        trace_name = request.node.name
        trace_dir = "test-results"
        os.makedirs(trace_dir, exist_ok = True)
        trace_path = os.path.join(trace_dir, f"trace-{trace_name}.zip")
        context.tracing.stop(path=trace_path)
    else:
        if request.node.rep_call.failed:
            test_name = request.node.name
            trace_dir = "test-results"
            os.makedirs(trace_dir, exist_ok=True)
            trace_path = os.path.join(trace_dir, f"trace-{test_name}.zip")
            context.tracing.stop(path=trace_path)
        else:
            context.tracing.stop()

@pytest.fixture(scope="function")
def setup_mobile_web(mobile_web_browser):
    page = mobile_web_context.new_page()
    yield page
    page.close()
