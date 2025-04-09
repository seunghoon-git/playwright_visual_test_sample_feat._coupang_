from pages.LoginPage import LoginPage
from pages.MyCoupang import MyCoupangPage
from pages.CartPage import Cart
import time
import re

class GateWay:

    def __init__(self, page):
        self.page = page
        self.login_button_in_header = page.locator(".top-bar").get_by_role("link", name="로그인", exact=True)
        self.logout_button_in_header = page.locator(".top-bar").get_by_role("link", name="로그아웃")
        self.customer_name_in_header = page.locator(".top-bar").locator("li#myCoupang")
        self.coupang_banner_above_of_header = page.locator("#coupang-banner")
        self.todays_hot = page.locator("#todaysHot")
        self.ads_side_bar = page.locator("section#contents").locator("#side-bar")
        # 오늘의 발견
        self.today_discovery_unit = page.locator("todayDiscorveryUnit").locator(".discouvery-list")
        # 오늘의 발견 아이템 리스트
        self.today_discovery_unit_list = page.locator("todayDiscorveryUnit").locator("//ul[@class='banner-list prod-list']/li").all()
        # 지금 이 상품이 필요하신가요?
        self.listing_carousel_now_needed = page.locator(".listing-carousel-body")
        # 오늘의 쇼핑 제안 & 좋아할만한 카테고리 상품
        self.decker_carousel = page.locator(".decker-carousel").all()
        # 프로모션 (오늘의 판매자 특가 & 전세계 핫딜 로켓직구 글로벌특가)
        self.promotion_decker_carousel = page.locator("personalizedGW").locator("//div[@class='promotion-decker-carousel']").all()
        self.promotion_today_seller_hot_deal = page.locator("personalizedGW").locator("//div[@class='gw_promotion carousel-widget-container ']//div[@class='promotion-carousel-body']")
        self.promotion_rocket_jikgu_hot_deal = page.locator("personalizedGW").locator("//div[@class='jikgu_promotion carousel-widget-container ']//div[@class='promotion-carousel-body']")
        #카테고리별 추천 광고상품
        self.category_best_unit_list = page.locator("#categoryBestUnit")
        self.category_best_digital = page.locator("#categoryBestUnit").locator("#categoryBest_digital")
        self.category_best_food = page.locator("#categoryBestUnit").locator("#categoryBest_food")
        self.category_best_beauty = page.locator("#categoryBestUnit").locator("#categoryBest_beauty")
        self.category_best_health = page.locator("#categoryBestUnit").locator("#categoryBest_health")
        self.category_best_living = page.locator("#categoryBestUnit").locator("#categoryBest_living")
        self.category_best_kitchen = page.locator("#categoryBestUnit").locator("#categoryBest_kitchen")
        self.category_best_woman_clothe = page.locator("#categoryBestUnit").locator("#categoryBest_womanclothe")
        self.category_best_man_clothe = page.locator("#categoryBestUnit").locator("#categoryBest_manclothe")
        self.category_best_decoration = page.locator("#categoryBestUnit").locator("#categoryBest_home_decoration")
        self.category_best_office = page.locator("#categoryBestUnit").locator("#categoryBest_office")
        self.category_best_sports = page.locator("#categoryBestUnit").locator("#categoryBest_sports")
        self.category_best_baby = page.locator("#categoryBestUnit").locator("#categoryBest_baby")
        self.category_best_baby_fashion = page.locator("#categoryBestUnit").locator("#categoryBest_babyfashion")
        self.category_best_pets = page.locator("#categoryBestUnit").locator("#categoryBest_pets")
        self.category_best_hobby = page.locator("#categoryBestUnit").locator("#categoryBest_hobby")
        self.category_best_car = page.locator("#categoryBestUnit").locator("#categoryBest_car")
        self.category_best_book = page.locator("#categoryBestUnit").locator("#categoryBest.book")
        self.category_best_travel = page.locator("#categoryBestUnit").locator("#categoryBest_travel")


        ######### mobile web #########
        # Banner
        self.go_app_banner = page.locator("#banner").locator("//a[@class='go-app-banner go-app']")
        self.go_app_banner_close_button = page.locator("#banner").locator("//button[@class='close-banner-icon-button']")

        self.whats_new_section = page.locator("#goodsList").locator("#whatsnew-section")
        self.gw_shortcuts = page.locator("#goodsList").locator("#gw-shortcusts")
        self.recommend_widget_container = page.locator("#goodsList").locator("#recommend-widget-container")
        self.recommend_widget_container_title = page.locator("#goodsList").locator(".recommend-widget__title")
        self.todays_hot_moweb = page.locator("#goodsList").locator("#TODAYS_HOT")
        self.beset_product = page.locator("#goodsList").locator("#BEST_PRODUCT")

        self.bottom_app_banner = page.locator("#BottomApppBanner").and_(page.locator("//div[@class='push']"))
        self.bottom_app_banner_close_button = page.locator("//div[@class='close-banner-warpper']")
        self.bottom_sheet_nudge_container = page.locator("//div[@class='bottom-sheet-nudge-container']")
        self.bottom_sheet_nudge_container_close_button = page.locator('#bottomSheetBudgeCloseButton')

        #GNB
        self.bottom_gnb = page.locator("nav#bottomMenu")
        self.gnb_category = page.locator("nav#bottomMenu").locator("a#bm_category")
        self.gnb_search = page.locator("nav#bottomMenu").locator("@#bm_search")
        self.gnb_coupang_home = page.locator("nav#bottomMenu").locator("a#home")
        self.gnb_my_coupang = page.locator("nav#bottomMenu").locator("a#bm_my")
        self.gnb_cart = page.locator("nav#bottomMenu").locator("a#cartBtn")
        self.gnb_cart_count = page.locator("nav#bottomMenu").locator("#gnbCartCnt")

        # Category
        self.category_title = page.locator("nav#category").get_by_role("heading", name = "카테고리")
        self.category_shopping = page.locator("nav#category").locator("h4").filter(has_text = '쇼핑 Shopping')
        self.category_travel_n_leisure = page.locator("nav#category").locatorr("h4").filter(has_text = '여행 Travel & Leisure')

        # Search
        self.search_input_field = page.locator("@searchBox").locator("span.input-search-wrap")
        self.search_close_button = page.locator("#searchBox").locator("#q_close")


    def click_login_button(self):
        self.login_button_in_header.click()
        time.sleep(1)

        login_page = LoginPage(self.page)
        return login_page
    
    def click_logout_button(self):
        self.logout_button_in_header.click()
        time.sleep(1)

    def click_moweb_gnb_my_coupang(self):
        self.gnb_by_coupang.click()
        time.sleep(1)

        my_coupang_page = MyCoupangPage(self.page)
        return my_coupang_page
    
    def click_moweb_gnb_cart(self):
        self.gnb_cart.click()
        time.sleep(1)

        cart_page = Cart(self.page)
        return cart_page

        