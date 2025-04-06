import time 
import re 

class MyCoupangPage: 
    def __init__(self, page):
        self.page = page
        self.gnb_menu_bar = page.locator("#full-gnb-header").locator("#gnb-meni-container")
        self.header_cart_count = page.locator("@full-gnb-header").locator("#headerCartCount")
        self.keen_slider_banner = page.locator("//div[contains(@class, 'keen-slider')]")
        self.promotion_banner_image_list = page.locator("//ul[@class='promotion-banner']/li/a/img").all()
        self.cart_count = page.locator('#side-bar').locator("div.side-cart")
        self.total_recently_viewed_products_section = page.locator('#side-bar').locator("div.recently-viewed-list")

        ################ mobile web elements ################
        self.mobile_web_header_cart_count = page.locator("header#coupang-header").locator("#gnbCartCnt")
        self.user_name = page.locator("@user-name")

        ## menu list
        self.menu_list = page.locator("#mclp_menu_list")
        self.btn_menu_order_list = page.locator("#mclp_menu_list").locator("#btn-menu-order-list")
        self.btn_menu_cancel_trn_exchange = page.locator("#mclp_menu_list").locator("#btn-menu-cancel-trn-exchange")
        self.btn_menu_gift_box = page.locator("#mclp_menu_list").locator("#btn-menu-gift-box")
        self.btn_menu_manage_review = page.locator("#mclp_menu_list").locator("#btn-menu-manage-review")
        self.btn_menu_wow_membership = page.locator("#mclp_menu_list").locator("#btn-menu-wow-membership")
        self.btn_menu_subscription_menu = page.locator("#mclp_menu_list").locator("#btn-menu-subscription-menu")
        self.btn_menu_regular_delivery = page.locator("#mclp_menu_list").locator("#btn-menu-regular-delivery")
        self.btn_menu_coupay = page.locator("#mclp_menu_list").locator("#btn-menu-coupay")
        self.btn_menu_freshbag = page.locator("#mclp_menu_list").locator("#btn-menu-freshbag")
        self.btn_menu_coupang_cash = page.locator("#mclp_menu_list").locator("#btn-menu-coupang-cash")
        self.btn_menu_discount_coupon = page.locator("#mclp_menu_list").locator("#btn-menu-discount-coupon")
        self.btn_menu_as = page.locator("#mclp_menu_list").locator("#btn-menu-as")
        self.btn_menu_cs_center = page.locator("#mclp_menu_list").locator("#btn-menu-cs-center")

        ## footer
        self.copyright = page.get_by_text(re.compile("Copyright © Coupang Corp. \\dd+-\\d+ All Rights Reserved."))

        ## GNB
        self.botton_gnb = page.locator("nav#bottomMenu")
        self.gnb_coupang_home = page.locator("nav#bottomMenu").get_by_role("link", name="쿠팡홈")
        self.gnb_category = page.locator("nav#bottomMenu").get_by_role("link", name="카테고리")
        self.gnb_search = page.locator("nav#bottomMenu").get_by_role("link", name="검색")
        self.gnb_my_coupang = page.locator("nav#bottomMenu").get_by_role("link", name="마이쿠팡")

    
    def click_moweb_gnb_coupang_home(self):
        from pages.GateWay import GateWay
        
        self.gnb_coupang_home.click()
        time.sleep(1)

        gate_way_page = GateWay(self.page)
        return gate_way_page
