from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.MyCoupang import MyCoupangPage
import re

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://mc.coupang.com/"
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.my_coupang
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_mycoupang_page_visual(assert_snapshot, setup_web_browser) -> None:
    page = setup_web_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    expect(login_page.page).to_have_url(re.compile(r"^"+target_url))

    mycoupang_page = MyCoupangPage(login_page.page)

    masking_list = [
        mycoupang_page.header_cart_count
        , mycoupang_page.keen_slider_banner
        , mycoupang_page.cart_count
        , mycoupang_page.total_recently_viewed_count
        , mycoupang_page.total_recently_viewed_products_section
    ]
    masking_list.extend(mycoupang_page.promotion_banner_image_list)

    assert_snapshot(mycoupang_page.page.screenshot(full_page = True, mask = masking_list))
    