from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.WowMembership import WowMembershipPage
import time

load_dotenv()
base_url = pytest.login_page_url
target_url = "https://loyalty.coupang.com/oaylty/management/home"
email = os.getenv("CORe_TEST_USER_PAID")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.loyalty
@pytest.mark.functional_test
@pytest.mark.regression_test
def test_cancel_and_resignup_wow_membership_via_wmp(setup_web_browser) -> None:
    page = setup_web_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, target_url)

    expect(login_page.page).to_have_url(target_url)

    wow_membership_page = WowMembershipPage(login_page.page)
    expect(wow_membership_page.coupay_money_balance).to_have_text('0')
    expect(wow_membership_page.user_badge).to_have_text("회원")
    expect(wow_membership_page.next_payment_date_text).to_be_visible()

    # ACTION : CLICK CANCELLATION CTA BUTTON AT THE BOTTOM OF WMP
    wow_membership_page.cancellation_button.scroll_into_view_if_needed()
    wow_membership_page.click_cancellation_cta_button_on_wmp
    
    # ACTION : CLICK CANCELLAION CTA BUTTON ON THE 1ST CANCELLATION PAGE
    wow_membership_page.first_cancellation_page_give_up_benefit_button.scroll_into_view_if_needed() 
    wow_membership_page.click_give_up_benefit_button_on_the_1st_cancellation_page()

    # ACTION : GIVE THE ANSWER FOR SURVYE AND CONTINUE
    wow_membership_page.answer_the_survey_option_5("This is for QA testing")
    wow_membership_page.click_cancellation_button_on_the_3rd_cancellation_page()

    # ACTION : CLICK CANCELLATION CTA BUTTON ON THE #RD CANCELLATION PAGE
    wow_membership_page.third_cancellation_page_cancel_button.scroll_into_view_if_needed()
    wow_membership_page.click_confirm_button_on_the_confirmation_popup()
    time.sleep(4)

    expect(wow_membership_page.coupay_money_balance).to_have_text('7,890')
    expect(wow_membership_page.user_badge).not_to_be_visible()
    expect(wow_membership_page.signup_cta_button).to_be_visible()

    # ACTION : SIGNUP WOW MEBERSHIP AGAIN
    wow_membership_page.click_signup_cta_button_on_wmp()
    time.sleep(3)

    expect(wow_membership_page.coupay_money_balance).to_have_text("0")
    expect(wow_membership_page.user_badge).to_have_text("회원")
    expect(wow_membership_page.next_payment_date_text).to_be_visible()
    