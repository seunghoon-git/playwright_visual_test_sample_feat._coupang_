from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.SignupFresh import SignupFreshPage
import time

load_dotenv()
base_url = pytest.login_page_url
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_fresh_page_visual_moweb_from_sdp_fresh_product(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=SDP&benefitType=FRESH_PRODUCT&serviceType=ROCKET_FRESH&welcomeCoupon=0&additionalCoupon=0&sourceDoamin=SDP"
    
    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")
    
    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupFreshPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(wow_signup_page.page.screenshot(full_page = True, mask = masking_list))


@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_fresh_page_visual_moweb_from_sdp_wow_cashback(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=SDP&benefitType=WOW_CASHBACK&serviceType=ROCKET_FRESH&welcomeCoupon=0&additionalCoupon=0&sourceDoamin=SDP"
    
    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")
    
    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupFreshPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(wow_signup_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_fresh_page_visual_moweb_from_sdp_atf_banner(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=sdp_atfBanner&benefitOnSource=wow_coupon_discount%2Cwow_coupon_discount&sdpWowSignUPIteration=true&wowOnlyInstantDiscount=0&wowPriceSelected=true&serviceType=ROCKET_FRESH&inScopeOfSdpFreshSignUpWow082=false"
    
    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")
    
    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupFreshPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(wow_signup_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_fresh_page_with_welcome_coupon_visual_moweb(assert_snapshot, setup_mobile_web) -> None:
    target_url = "https://loyalty.coupang.com/m/loyalty/sign-up/intro?source=SDP&benefitType=FRESH_PRODUCT&serviceType=ROCKET_FRESH&welcomeCoupon=18000&additionalCoupon=0&sourceDomain=SDP"
    
    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")
    
    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_signup_page = SignupFreshPage(login_page.page)
    wow_signup_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [wow_signup_page.benefit_carousel]
    assert_snapshot(wow_signup_page.page.screenshot(full_page = True, mask = masking_list))