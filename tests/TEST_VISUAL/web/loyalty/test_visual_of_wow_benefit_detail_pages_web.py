from playwright.sync_api import Page, expect
import pytest
import time

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_SHIPPING_THRESHOLD_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=SHIPPING_THRESHOLD&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_DAUM_DELIVERY_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=DAWM_DELIVERY&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_SAMEDAY_DELIVERY_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=SAMEDAY_DELIVERY&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_JIKGU_PRODUCT_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=JIKGU_PRODUCT&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_FRESH_PRODUCT_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=FRESH_PRODUCT&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_WOW_DISCOUNT_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=WOW_DISCOUNT&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_EXCLUSIVE_PRICE_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=EXCLUSIVE_PRICE&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail__page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_TIME_DISCOUNT_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=TIME_DISCOUNT&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_TRAVEL_DISCOUNT_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=TRAVEL_DISCOUNT&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_WOW_CASHBACK_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=WOW_CASHBACK&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_PLAY_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=PLAY&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

@pytest.mark.loyalty
@pytest.mark.visual_test
@pytest.mark.regression_test
def test_wow_benefit_detail_EATS_page_visual(assert_snapshot, setup_web_browser_popup) -> None:
    target_url = "https://loyalty.coupang.com/loyalty/benefit/benefit-detail?benefitType=EATS&source=membership_management"

    page = setup_web_browser_popup
    page.goto(target_url)
    page.wait_for_load_state("load")

    expect(page).to_have_url(target_url)
    
    assert_snapshot(page.screenshot(full_page = True))

