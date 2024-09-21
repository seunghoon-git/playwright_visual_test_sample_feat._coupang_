from pages.LoginPage import LoginPage
from playwright.sync_api import Page, expect
import pytest

base_url = "https://login.coupang.com/login/login.pang"

@pytest.mark.visual_test
def test_email_login_page_visual(assert_snapshot, setup_browser) -> None:
    page = setup_browser
    page.goto(base_url)
    page.wait_for_load_state("load")
                             
    expect(page).to_have_url(base_url)

    login_page = LoginPage(page)
    assert_snapshot(login_page.page.screenshot(full_page = True))


@pytest.mark.visual_test
def test_phone_number_login_page_visual(assert_snapshot, setup_browser) -> None:
    page = setup_browser
    page.goto(base_url)
    page.wait_for_load_state("load")
                             
    expect(page).to_have_url(base_url)

    login_page = LoginPage(page)
    login_page.select_phone_number_login()
    assert_snapshot(login_page.page.screenshot(full_page = True))


@pytest.mark.visual_test
def test_qr_login_page_visual(assert_snapshot, setup_browser) -> None:
    page = setup_browser
    page.goto(base_url)
    page.wait_for_load_state("load")
                             
    expect(page).to_have_url(base_url)

    login_page = LoginPage(page)
    login_page.select_qr_login()
    masking_list = [login_page.qr_login_number, login_page.qr_login_image, login_page.qr_login_timer]
    assert_snapshot(login_page.page.screenshot(full_page = True, mask = masking_list))
