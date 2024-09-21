import pytest


@pytest.fixture(scope = 'function')
def setup_browser(page):
    page.set_viewport_size({"width": 1470, "height": 750})
    #page.set_viewport_size({}"width": 1536, "height": 800})
    yield page