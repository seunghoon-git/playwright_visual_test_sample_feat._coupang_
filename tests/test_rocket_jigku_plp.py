from utils import util
from pages.RocketJikgu import RocketJikguPLP
from playwright.sync_api import Page, expect
import pytest

base_url = "https://www.coupang.com/np/coupangglobal"

@pytest.mark.visual_test
def test_rocket_fresh_plp_full_page_visual(assert_snapshot, setup_browser) -> None:
    page = setup_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    page = util.page_scroll_down(page, scroll_count = -1)

    expect(page).to_have_url(base_url)

    rj_plp_page = RocketJikguPLP(page)
    masking_list = [rj_plp_page.coupang_banner, rj_plp_page.main_banner_list, rj_plp_page.filter_option_brand]
    masking_list.extend(rj_plp_page.multi_link_banner)
    masking_list.extend(rj_plp_page.product_list)

    assert_snapshot(rj_plp_page.page.screenshot(full_page = True, mask = masking_list))