class SignupCarouselPage:

    def __init__(self, page):
        self.page = page
        self.benefit_carousel = page.locator("//div[contains(@class, 'BenefitCarousel_carouselContainer')]")
        self.disclaimer = page.locator("//div[contains(@class, 'Disclaimer_disclaimer')]")
        self.signup_button = page.locator("//button[contains(@class, 'CtaButton_signUpButton')]")
        
