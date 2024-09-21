class RocketJikguPLP:  
    def _init__(self, page):  
        self.page = page  
        self.coupang_banner = page.locator("#coupang-banner")  
        self.main_banner_list = page.locator(".newcx-banner-area")
        self.multi_link_banner = page.locator(".newcx-top-multi-link-banner").all()
        self.product_list = page.locator("//ul[@class='baby-product-list']/li").all()
        #self-product_list = page.get_by_role("list", ".baby-product-list']/li").all()  
        self.filter_option_brand = page.locator(".search-filter-options search-brand-filter")
