from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.WowMembership import WowMembershipPage
import time

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://loyalty.coupang.com/loyalty/management/home"

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membershipt_page_visual_not_member(assert_snapshot, setup_web_browser) -> None:
    email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_web_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    time.sleep(2)
    expect(login_page.page).to_have_url(target_url)

    wow_membership_page = WowMembershipPage(login_page.page)

    masking_list = [
        wow_membership_page.header_cart_count
        , wow_membership_page.cart_count
        , wow_membership_page.total__viewed_count
        , wow_membership_page._viewed_products_section 
    ]

    masking_list.extend(wow_membership_page.promotion_banner_image_list)

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mas = masking_list))


@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_paid_member_no_bud(assert_snapshot, setup_web_browser) -> None:
    email = os.getenv("CORE_TEST_USER_PAID")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_web_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    time.sleep(2)
    expect(login_page.page).to_have_url(target_url)

    wow_membership_page = WowMembershipPage(login_page.page)
    expect(wow_membership_page.next_payment_date_text).to_be_visible()

    masking_list = [
        wow_membership_page.header_cart_count
        , wow_membership_page.coupay_money_balance_section
        , wow_membership_page.coupang_cash_balance_section
        , wow_membership_page.next_payment_date_text_area
        , wow_membership_page.coupang_play_intro_image
        , wow_membership_page.cart_count
        , wow_membership_page.total_recently_viewed_count
        , wow_membership_page.recently_viewed_products_section
    ]
    masking_list.extend(wow_membership_page.promotion_banner_image_list)

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_paid_member_bud(assert_snapshot, setup_web_browser) -> None:
    email = os.getenv("CORE_TEST_USER_EMAIL")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_web_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    time.sleep(2)
    expect(login_page.page).to_have_url(target_url)

    wow_membership_page = WowMembershipPage(login_page.page)
    expect(wow_membership_page.next_payment_date_text).to_be_visible()

    masking_list = [
        wow_membership_page.header_cart_count
        , wow_membership_page.coupay_money_balance_section
        , wow_membership_page.coupang_cash_balance_section
        , wow_membership_page.next_payment_date_text_area
        , wow_membership_page.bud_total
        , wow_membership_page.bud_detail
        , wow_membership_page.bud_desc
        , wow_membership_page.coupang_play_intro_image
        , wow_membership_page.cart_count
        , wow_membership_page.total_recently_viewed_count
        , wow_membership_page.recently_viewed_products_section
    ]
    masking_list.extend(wow_membership_page.promotion_banner_image_list)

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list))
                
@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_page_visual_onhold(assert_snapshot, setup_web_browser) -> None:
    email = os.getenv("CORE_TEST_USER_ON_HOLD")
    password = os.getenv("CORE_TEST_USER_PASSWORD")

    page = setup_web_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    time.sleep(2)
    expect(login_page.page).to_have_url(target_url)

    wow_membership_page = WowMembershipPage(login_page.page)

    masking_list = [
        wow_membership_page.header_cart_count
        , wow_membership_page.cart_count
        , wow_membership_page.total_recently_viewed_count
        , wow_membership_page.recently_viewed_products_section
    ]
    masking_list.extend(wow_membership_page.promotion_banner_image_list)

    assert_snapshot(wow_membership_page.page.screenshot(full_page = True, mask = masking_list))
                