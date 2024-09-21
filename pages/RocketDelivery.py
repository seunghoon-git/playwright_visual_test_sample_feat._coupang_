class RocketDeliveryPLP:
    def _init__(self, page):
        self.page = page 
        self.coupang_banner = page.locator("#coupang-banner")
        self.main_banner_list = page.locator(".newcx-banner-area")
        self.multi_banner_continer = page.locator(".newcx-widget-multi-baner-container").all()
        self.multi_link_banner = page.locator(".newcx-top-multi-link-banner")
        self.product_list = page.locator("//ul[@class='baby-product-list']/li").all()