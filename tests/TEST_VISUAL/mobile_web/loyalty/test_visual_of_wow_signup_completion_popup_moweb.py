from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
import time

load_dotenv()
base_url = pytest.login_page_url
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORe_TEST_USER_PASSWORD")

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_completion_popup_visual(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/node/sign-up/complete"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)

    assert_snapshot(login_page.page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_completion_popup_visual(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/node/sign-up/complete/bottom-sheet?wowcardNudgeWhenSignupComplete=B"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)

    assert_snapshot(page.screenshot(full_page = True))
