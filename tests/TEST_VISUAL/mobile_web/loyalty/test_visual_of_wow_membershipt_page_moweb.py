from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.WowMembership import WowMembershipPage
import time

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://loyalty.coupang.com/m/loyalty/management/home"
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membershipt_page_visual_moweb_not_member(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_NOT_MEMBER")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [wow_membership_page.top_gnb_cart_count]
    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mas = masking_list), threshold = 0.2)

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_moweb_paid_member_no_bud(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_PAID")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(2)

    expect(login_page.page).to_have_url(target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [
        wow_membership_page.top_gnb_cart_count
        , wow_membership_page.moweb_next_payment_date_text_area
        , wow_membership_page.coupang_play_intro_image
    ]

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.2)

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_moweb_paid_member_bud(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_EMAIL")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(2)

    expect(login_page.page).to_have_url(target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [
        wow_membership_page.top_gnb_cart_count
        , wow_membership_page.moweb_next_payment_date_text_area
        , wow_membership_page.coupang_play_intro_image
        , wow_membership_page.bud_total
        , wow_membership_page.bud_detail
    ]

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.2)
                
@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_moweb_onhold(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_ON_HOLD")

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)
    time.sleep(2)

    expect(login_page.page).to_have_url(target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [
        wow_membership_page.top_gnb_cart_count
        , wow_membership_page.on_hold_temporary_suspension_period
    ]

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.3)

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membershipt_page_visual_moweb_not_member_from_eats(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
    modified_target_url = target_url + "?source=EATS&sourceV2=EATS_MYEATS_WOWSIGNUP&benefitOnSource=eats_discount"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    time.sleep(1)

    expect(login_page.page).to_have_url(modified_target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [wow_membership_page.top_gnb_cart_count]
    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mas = masking_list), threshold = 0.2)

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_moweb_paid_member_no_BUD_from_eats(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_PAID")
    modified_target_url = target_url + "?source=EATS&sourceV2=EATS_MYEATS_WOWSIGNUP&benefitOnSource=eats_discount"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    time.sleep(2)

    expect(login_page.page).to_have_url(modified_target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [
        wow_membership_page.top_gnb_cart_count
        , wow_membership_page.moweb_next_payment_date_text_area
        , wow_membership_page.coupang_play_intro_image
    ]

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.2)

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_moweb_paid_member_BUD_from_eats(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_EMAIL")
    modified_target_url = target_url + "?source=EATS&sourceV2=EATS_MYEATS_WOWSIGNUP&benefitOnSource=eats_discount"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    time.sleep(2)

    expect(login_page.page).to_have_url(modified_target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [
        wow_membership_page.top_gnb_cart_count
        , wow_membership_page.moweb_next_payment_date_text_area
        , wow_membership_page.coupang_play_intro_image
        , wow_membership_page.bud_total
        , wow_membership_page.bud_detail
    ]

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.2)
                
@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_moweb_onhold_from_eats(assert_snapshot, setup_mobile_web) -> None:
    email = os.getenv("CORE_TEST_USER_ON_HOLD")
    modified_target_url = target_url + "?source=EATS&sourceV2=EATS_MYEATS_WOWSIGNUP&benefitOnSource=eats_discount"

    page = setup_mobile_web
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    time.sleep(2)

    expect(login_page.page).to_have_url(modified_target_url)
    wow_membership_page = WowMembershipPage(login_page.page)
    wow_membership_page.wow_benefits_last_item.scroll_into_view_if_needed()

    masking_list = [
        wow_membership_page.top_gnb_cart_count
        , wow_membership_page.on_hold_temporary_suspension_period
    ]

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.3)
