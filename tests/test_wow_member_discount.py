from utils import util
from pages.WowMemberDiscount import WowMemberDiscount
from playwright.sync_api import Page, expect
import pytest

base_url = "https://www.coupang.com/np/campaigns/83"

@pytest.mark.visual_test
def test_rocket_fresh_plp_full_page_visual(assert_snapshot, setup_browser) -> None:
    page = setup_browser
    page.goto(base_url)
    page.wait_for_load_state("load")

    page = util.page_scroll_down(page, scroll_count = -1)

    expect(page).to_have_url(base_url)

    wmd_page = WowMemberDiscount(page)
    masking_list = [wmd_page.coupang_banner, wmd_page.filter_option_brand]
    masking_list.extend(wmd_page.multi_link_banner)
    masking_list.extend(wmd_page.product_list)

    assert_snapshot(wmd_page.page.screenshot(full_page = True, mask = masking_list))