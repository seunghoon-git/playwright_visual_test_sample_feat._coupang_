class GateWay:

    def _init__(self, page):
        self.page = page
        self.coupang_banner = page.locator("#coupang-banner")
        self.todays_hot = page.locator("#todaysHot")
        self.ads_side_bar = page.locator("#side-bar")
        # 오늘의 발견
        self.today_discovery_unit = page.locator("//div[@class='discovery-list']")
        # 오늘의 발견 아이템 리스트
        self.today_discovery_unit_list = page.locator("//ul[@class='banner-list prod-list']/li").all()
        # 지금 이 상품이 필요하신가요?
        self.listing_carousel_now_needed = page.locator("//div [@class='listing-carousel-body']")
        # 오늘의 쇼핑 제안 & 좋아할만한 카테고리 상품
        self.decker_carousel = page.locator("//div [@class='decker-carousel']").all()
        # 프로모션 (오늘의 판매자 특가 & 전세계 핫딜 로켓직구 글로벌특가)
        self.promotion_decker_carousel = page.locator("//div[@class='promotion-decker-carousel']").all()
        self.promotion_today_seller_hot_deal = page.locator("//div[@class='gw_promotion carousel-widget-container ']//div[@class='promotion-carousel-body']")
        self.promotion_rocket_jikgu_hot_deal = page.locator("//div[@class='jikgu_promotion carousel-widget-container ']//div[@class='promotion-carousel-body']")
        #카테고리별 추천 광고상품
        self.category_best_unit_list = page.locator("#categoryBestUnit")
        self.category_best_digital = page.locator("#categoryBest_digital")
        self.category_best_food = page.locator("#categoryBest_food")
        self.category_best_beauty = page.locator("#categoryBest_beauty")
        self.category_best_health = page.locator("#categoryBest_health")
        self.category_best_living = page.locator("#categoryBest_living")
        self.category_best_kitchen = page.locator("#categoryBest_kitchen")
        self.category_best_woman_clothe = page.locator("#categoryBest_womanclothe")
        self.category_best_man_clothe = page.locator("#categoryBest_manclothe")
        self.category_best_decoration = page.locator("#categoryBest_home_decoration")
        self.category_best_office = page.locator("#categoryBest_office")
        self.category_best_sports = page.locator("#categoryBest_sports")
        self.category_best_baby = page.locator("#categoryBest_baby")
        self.category_best_baby_fashion = page.locator("#categoryBest_babyfashion")
        self.category_best_pets = page.locator("#categoryBest_pets")
        self.category_best_hobby = page.locator("#categoryBest_hobby")
        self.category_best_car = page.locator("#categoryBest_car")
        self.category_best_book = page.locator("#categoryBest.book")
        self.category_best_travel = page.locator("#categoryBest_travel")


        