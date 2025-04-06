class SignupDefaultVerticalPage:

    def __init__(self, page):
        self.page = page
        self.count_down_time = page.locator("//div[contains(@class, 'CountdownTimer_time')]").all()
        self.gold_box_product_list = page.locator("//div[contains(@class, 'GoldBoxProducts_scrollable')]")
        self.disclaimer = page.locator("//div[contains(@class, 'Disclaimer_disclaimer')]")
        self.signup_button = page.locator("//button[contains(@class, 'CtaButton_signUpButton')]")

        