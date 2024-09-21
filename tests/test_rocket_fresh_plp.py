from utils import util
from pages.RocketFresh import RocketFreshPLP
from playwright.sync_api import Page, expect
import pytest

base_url = "https://www.coupang.com/np/campaigns/393760"

@pytest.mark.visual_test
def test_rocket_fresh_plp_full_page_visual(assert_snapshot, setup_browser) -> None:
    page = setup_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    page = util.page_scroll_down(page, scroll_count = -1)

    expect(page).to_have_url(base_url)

    rf_plp_page = RocketFreshPLP(page)
    masking_list = [rf_plp_page.coupang_banner, rf_plp_page.main_banner_list, rf_plp_page.multi_link_banner]
    masking_list.extend(rf_plp_page.multi_banner_continer)
    masking_list.extend(rf_plp_page.product_list)

    assert_snapshot(rf_plp_page.page.screenshot(full_page = True, mask = masking_list))