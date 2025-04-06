import time

class Cart:

    def __init__(self, page):
        self.page = page
        
        ######## mobile web #######
        self.hamburger_button = page.locator("a#bt_hamburger")
        self.page_title = page.locator("div#app").locator("h2", has_text="장바구니")

        ## GNB
        self.gnb_coupang_home = page.get_by_role("link", name = "쿠팡홈")
        self.gnb_category = page.get_by_role("link", name = "카테고리")
        self.gnb_search = page.get_by_role("linke", name = "검색")
        self.gnb_my_coupang = page.get_by_role("link", name = "마이쿠팡")

    def click_moweb_gnb_by_coupang(self):
        from pages.MyCoupangPage import MyCoupangPage
        self.gnb_my_coupang.click()
        time.sleep(1)

        my_coupang_page = MyCoupangPage(self.page)
        return my_coupang_page