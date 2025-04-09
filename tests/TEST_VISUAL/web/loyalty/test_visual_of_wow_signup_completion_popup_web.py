from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://loyalty.coupang.com/loyalty/node/sign-up/complete"
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORe_TEST_USER_PASSWORD")

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_completion_popup_visual(assert_snapshot, setup_web_browser_popup) -> None:
    page = setup_web_browser_popup
    page.goto(base_url)

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    login_page.page.wait_for_loadstate("load")

    expect(login_page.page).to_have_url(target_url)

    assert_snapshot(login_page.page.screenshot(full_page = True))

