from utils import util
from pages.GateWay import GateWay
from playwright.sync_api import Page, expect
import pytest

base_url = "https://www.coupang.com"

@pytest.mark.visual_test
def test_gateway_initial_loading_full_page_visual(assert_snapshot, setup_browser) -> None:
    error_log = []
    page = setup_browser
    page.on("console", lambda msg: error_log.append(f"error: {msg}") if msg.type == "error" else None)
    page.goto(base_url)
    page.wait_for_load_state("load")

    page = util.page_scroll_down(page, scroll_count = -1)

    expect(page).to_have_url(base_url)

    gw_page = GateWay(page)
    
    ## Masking 영역 지정 ##
    masking_list = [gw_page.coupang_banner, gw_page.todays_hot, gw_page.ads_side_bar, gw_page.listing_carousel_now_needed]
    masking_list += [gw_page.category_best_digital, gw_page.category_best_food, gw_page.category_best_beauty, gw_page.category_best_health,
                     gw_page.category_best_living, gw_page.category_best_kitchen, gw_page.category_best_woman_clothe,
                     gw_page.category_best_man_clothe, gw_page.category_best_decoration, gw_page.category_best_office,
                     gw_page.category_best_sports, gw_page.category_best_baby, gw_page.category_best_baby_fashion,
                     gw_page.category_best_pets, gw_page.category_best_hobby, gw_page.category_best_car, gw_page.category_best_book,
                     gw_page.category_best_travel]
    
    masking_list.extend(gw_page.promotion_decker_carousel)
    masking_list.extend(gw_page.today_discovery_unit_list)
    #######HHHHH+###  
    
    if len(gw_page.promotion_decker_carousel) > 1:
        assert_snapshot(gw_page.page.screenshot(full_page = True, mask = masking_list), threshold = 0.3, name = "test_gateway_initial_loading_full_page_with_seller_n_jikgu_promotion.png")  
    else:
        if gw_page.promotion_today_seller_hot_deal.count():
            assert_snapshot(gw_page.page.screenshot(full_page = True, mask = masking_list), name = 'test_gateway initial_loading full page_with_seller_promotion.png')
        elif gw_page.promotion_rocket_jikgu_hot_deal.count():
            assert_snapshot(gw_page.page.screenshot(full_page = True, mask = masking_list), name = 'test gateway_initial loading full_page with jikgu_promotion.png')
