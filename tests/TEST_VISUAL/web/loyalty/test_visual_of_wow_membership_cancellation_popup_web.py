from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.WowMembershipCancellation import WowMembershipCancellationPopup1
from pages.WowMembershipCancellation import WowMembershipCancellationPopup3
import time

load_dotenv()
email = os.getenv("CORE_TEST_USER_PAID")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_cancellation_step1_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/management/withdraw-popup"

    page = setup_web_browser_popup
    page.goto(pytest.login_page_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    expect(page).to_have_url(target_url)
    cancellation_step1 = WowMembershipCancellationPopup1(page)

    masking_list = [cancellation_step1.remaining_days_text, cancellation_step1.benefit_play_carousel]
    assert_snapshot(cancellation_step1.page.screenshot(full_page = True, mask = masking_list), threshold = 0.2)

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_cancellation_step2_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/management/withdraw/survey"

    page = setup_web_browser_popup
    page.goto(pytest.login_page_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    expect(page).to_have_url(target_url)
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_membership_cancellation_step3_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/management/withdraw-request/refund"

    page = setup_web_browser_popup
    page.goto(pytest.login_page_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    expect(login_page.page).to_have_url(target_url)

    cancellation_step3 = WowMembershipCancellationPopup3(login_page.page)
    cancellation_step3.cancel_button.scroll_into_view_if_needed()

    assert_snapshot(cancellation_step3.page.screenshot(full_page = True))



