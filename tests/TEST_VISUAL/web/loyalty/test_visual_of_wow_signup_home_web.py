from playwright.sync_api import Page, expect
import pytest

target_url = "https://loyalty.coupang.com/loyalty/sign-up/home"

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_home_page_visual(assert_snapshot, setup_web_browser) -> None:
    page = setup_web_browser
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)

    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_signup_home_page_visual_from_Goldbox(assert_snapshot, setup_web_browser) -> None:
    modified_target_url = terget_url = "?source=GOLDBOX"
    page = setup_web_browser
    page.goto(modified_target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(modified_target_url)

    assert_snapshot(page.screenshot(full_page = True))


