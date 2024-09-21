import re

class WowMemberDiscount:
    def __init__(self, page): 
        self.page = page 
        self.coupang_banner = page.locator("#coupang-banner") 
        self.multi_link_banner = page.locator(".newcx-top-multi-link-banner").all() 
        self.product_list = page.locator("//ul[@class='baby-product-list']/li").all() 
        self.filter_option_brand = page.locator("//div[@class='search-filter-options search-brand-filter']")
        #self.filter_option_brand = page.locator(".search-filter-options search-brand-filter") #for some reason, element is not found by this
        #self.filter_option_attribute_list = page.locator(re.compile("//div[@class='search-filter-options search-attr_*\'\]")).all()