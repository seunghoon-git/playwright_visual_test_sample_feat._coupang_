from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.MyCoupang import MyCoupangPage
import time

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://mc.coupang.com/"

@pytest.mark.my_coupang
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_mycoupang_page_visual(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url+'ssr')
    mycoupang_page = MyCoupangPage(login_page.page)

    masking_list = [mycoupang_page.mobile_web_header_cart_count]
    
    assert_snapshot(mycoupang_page.page.screenshot(full_page = True, mask = masking_list))
    