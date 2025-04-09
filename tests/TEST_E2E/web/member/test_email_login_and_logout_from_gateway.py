from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.GateWay import GateWay
import time

load_dotenv()
target_url = pytest.coupang_home_url
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.member
@pytest.mark.functional_test
@pytest.mark.regression_test
def test_email_login(setup_web_browser) -> None:
    page = setup_web_browser
    
    # Landing on GateWay page
    page.goto(target_url)
    page.wait_for_load_state("load")
    expect(page).to_have_url(target_url)
    gw_page = GateWay(page)

    # Clicking login button
    login_page = gw_page.click_login_button()

    # Logging in with email
    login_page.login_with_email(email, password)

    # Verifying Login
    expect(gw_page.customer_name_in_header).to_be_visible()
    expect(gw_page.coupang_banner_above_of_header).to_be_visible()

    # Logging out
    gw_page.click_logout_button()
    expect(gw_page.login_button_in_header).to_be_visible()