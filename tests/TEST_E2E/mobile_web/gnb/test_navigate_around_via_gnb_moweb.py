from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.GateWay import GateWay
import time

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://m.coupang.com/"

@pytest.mark.functional_test
@pytest.mark.regression_test
def test_navigate_around_via_gnb_moweb(setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password)

    # Check if it lands on mobile coupang home
    expect(login_page.page).to_have_url(target_url)
    gw_page = GateWay(login_page.page)
    gw_page.page.wait_for_load_state("load")
    time.sleep(3)

    max_check = 5
    go_app_banner = gw_page.go_app_banner.is_visible()
    bottom_app_banner = gw_page.bottom_app_banner.is_visible()

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
    
    # Check Gateway elements
    expect(gw_page.bottom_gnb).to_be_visible()
    expect(gw_page.whats_new_section).to_be_visible()
    expect(gw_page.gw_shortcuts).to_be_visible()

    # Click Category
    gw_page.gnb_category.click()
    time.sleep(1)
    expect(gw_page.category_title).to_be_visible()
    expect(gw_page.category_shopping).to_be_visible()
    expect(gw_page.category_travel_n_leisure).to_be_visible()
    
    # Click Search
    gw_page.gnb_search.click()
    time.sleep(1)
    expect(gw_page.search_input_field).to_be_visible()
    expect(gw_page.search_close_button).to_be_visible()
    gw_page.search_close_button.click()
    expect(gw_page.search_input_field).not_to_be_visible()
    expect(gw_page.search_close_button).not_to_be_visible()

    # Click Cart
    cart_page = gw_page.click_moweb_gnb_cart()
    time.sleep(1)
    expect(cart_page.page_title).to_be_visible()
    cart_page.hamburger_button.click()
    cart_page.gnb_my_coupang.click()

    # Click My Coupang
    my_coupang_page = cart_page.click_moweb_gnb_my_coupang()
    expect(my_coupang_page.page).to_have_url("https://mc.coupang.com/ssr")
    expect(my_coupang_page.user_name).to_be_visible()
    time.sleep(1)

    # Click Coupang Home
    gate_way_2 = my_coupang_page.click_moweb_gnb_coupang_home()
    time.sleep(1)
    expect(gate_way_2.page).to_have_url(target_url)