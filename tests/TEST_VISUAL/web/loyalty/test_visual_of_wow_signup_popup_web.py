from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv
from pages.LoginPage import LoginPage
from pages.SignupDefaultVertical import SignupDefaultVerticalPage

load_dotenv()
target_url = "https://loyalty.coupang.com/loyalty/sign-up.intro"
email = os.getenv("CORE_TEST_USER_NOT_MEMBER")
password = os.getenv("CORE_TEST_USER_PASSWORD")

@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_popup_visual_from_wow_ccid(assert_snapshot, setup_web_browser_popup) -> None:
    modified_target_url = target_url + "?source=sdp_wow_only_ccid$benefitType=WOW_CCID"
    page = setup_web_browser_popup
    page.goto(pytest.login_page_url)

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    login_page.page.wait_for_load_state("load")

    expect(login_page.page).to_have_url(modified_target_url)

    signup_default_vertical_page = SignupDefaultVerticalPage(login_page.page)
    signup_default_vertical_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [signup_default_vertical_page.gold_box_product_list]
    masking_list.extend(signup_default_vertical_page.count_down_timer)
    assert_snapshot(signup_default_vertical_page.page.screenshot(full_page = True, mask = masking_list))


@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_popup_visual_from_checkout(assert_snapshot, setup_web_browser_popup) -> None:
    modified_target_url = target_url + "?source=checkout"
    page = setup_web_browser_popup
    page.goto(pytest.login_page_url)

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    login_page.page.wait_for_load_state("load")

    expect(login_page.page).to_have_url(modified_target_url)

    signup_default_vertical_page = SignupDefaultVerticalPage(login_page.page)
    signup_default_vertical_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [signup_default_vertical_page.gold_box_product_list]
    masking_list.extend(signup_default_vertical_page.count_down_timer)
    assert_snapshot(signup_default_vertical_page.page.screenshot(full_page = True, mask = masking_list))


@pytest.mark.loaylty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_popup_visual_from_fresh(assert_snapshot, setup_web_browser_popup) -> None:
    modified_target_url = target_url + "?source=SDP&benefitType=FRESH_PRODUCT"
    page = setup_web_browser_popup
    page.goto(pytest.login_page_url)

    login_page = LoginPage(page)
    login_page.login_with_email(email, password, modified_target_url)
    login_page.page.wait_for_load_state("load")

    expect(login_page.page).to_have_url(modified_target_url)

    signup_default_vertical_page = SignupDefaultVerticalPage(login_page.page)
    signup_default_vertical_page.disclaimer.scroll_into_view_if_neede()

    masking_list = [signup_default_vertical_page.gold_box_product_list]
    masking_list.extend(signup_default_vertical_page.count_down_timer)
    assert_snapshot(signup_default_vertical_page.page.screenshot(full_page = True, mask = masking_list))
