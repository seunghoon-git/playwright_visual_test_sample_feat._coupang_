from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.GateWay import GateWay
import time

load_dotenv()
base_url = pytest.login_page_url
target_url = pytest.coupang_mobile_web_home_url

@pytest.mark.visual_test
@pytest.mark.regression_test
def test_gateway_first_view_port_visual_moweb(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password)
    time.sleep(3)

    expect(login_page.page).to_have_url(target_url)
    gw_page = GateWay(login_page.page)
    gw_page.page.wait_for_load_state("load")
    time.sleep(3)

    max_check = 5
    go_app_banner = gw_page.go_app_banner.is_visible()
    bottom_app_banner = gw_page.bottom_app_banner.is_visible()
    bottom_sheet_nudge = gw_page.bottom_sheet_nudge_container.is_visible()

    while max_check>0 and (go_app_banner | bottom_app_banner | bottom_sheet_nudge):
        print(max_check)
        if go_app_banner and gw_page.go_app_banner.is_visible():
            gw_page.go_app_banner_close_button.click()
            go_app_banner = False
            time.sleep(0.5)
        elif bottom_sheet_nudge and gw_page.bottom_sheet_nudge_container.is_visible():
            gw_page.bottom_sheet_nudge_container_close_button.click()
            bottom_sheet_nudge = False
            time.sleep(0.5)
        elif bottom_app_banner and gw_page.bottom_app_banner.is_visible():
            gw_page.bottom_app_banner_close_button.click()
            bottom_app_banner = False
            time.sleep(0.5)
        
        max_check -= 1

    expect(gw_page.bottom_gnb).to_be_visible()

    masking_list = [
        gw_page.whats_new_section
        , gw_page.todays_hot_moweb
        , gw_page.beset_product
        , gw_page.gnb_cart_count
    ]

    assert_snapshot(gw_page.page.screenshot(mask = masking_list), threshold = 0.2)

