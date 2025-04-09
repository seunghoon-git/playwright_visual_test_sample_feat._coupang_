from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.SignupCarousel import SignupCarouselPage
import time

load_dotenv()
base_url = pytest.login_page_url
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_carousel_page_visual_from_gw_nudge_moweb(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=PROMOTION_HEADER&benefitType=DEFAULT"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupCarouselPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_needed()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(login_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_carousel_page_visual_from_goldbox_moweb(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=benefitType=EXCLUSIVE_PRICE"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupCarouselPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_needed()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(login_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_carousel_page_with_welcome_coupon_visual_moweb(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=sdp_handler&benefitType=EXCLUSIVE_PRICE"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupCarouselPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_needed()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(login_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_carousel_page_with_ccid_visual_moweb(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=sdp_wow_only_ccid&benefitType=WOW_CCID"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupCarouselPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_needed()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(login_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_carousel_page_with_wow_discount_visual_moweb(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=SDP_DISCOUNTNUDGE&benefitType=EXCLUSIVE_PRICE"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupCarouselPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_needed()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(login_page.page.screenshot(full_page = True, mask = masking_list))
