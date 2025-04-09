from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
import time
import re

load_dotenv()
base_url = pytest.login_page_url
signup_page_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?benefitType=EXCLUSIVE_PRICE"
target_url = "https://loyalty.coupang.com/loyalty/sign-up/exception?type=ALREADY_MEMBER"
email = os.getenv("CORE_TEST_USER_PAID")
password = os.getenv("CORE_TEST)USER_PASSWORD")


@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_home_page_visual_moweb(assert_snapshot, setup_mobile_web) -> None:
    page = setup_mobile_web
    page.goto(base_url)

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, signup_page_url)
    time.sleep(1)
    
    expect(login_page.page).to_have_url(re.compile(r"^"+target_url))
    
    assert_snapshot(page.screenshot(full_page = True))