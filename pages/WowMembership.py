import re

class WowMembershipPage:

    def __init__(self, page):
        self.page = page
        self.gnb_menu_bar = page.locator("#gnb-menu-container")
        self.header_cart_count = page.locator("#header-cart-count")
        self.coupay_money_balance = page.locator("#coupayMoneyBalance")
        self.coupay_money_balance_section = page.get_by_text(re.compile("쿠페이 머니[0-9,]+원"))
        self.coupay_cash_balance = page.locator("#coupayCashBalance")
        self.coupay_cash_balance_section = page.get_by_text(re.compile("쿠팡캐시[0-9,]+원"))

        # Wow membership management
        self.user_badge = page.locator("//div[contains(@class, 'Main_head-line__badge)]")
        self.signup_cta_button = page.locator("//button[contains(@class, 'MainNonMember_landing-btn')]")
        self.next_payment_date_text_area = page.locator("//div[contains(@class, 'Main_next-date-tip-2')]")
        self.next_payment_date_text = page.get_by_text(re.compile("다음 결제 예정일은 \\d+년 \\d+월 \\d+일 입니다"))
        self.bud_total = page.locator("//div[contains(@class, 'monetaryDiscountUsageTable_total-price')]")
        self.bud_detail = page.locator("//div[contains(@class, 'monetaryDiscountUsageTable_benefit-table')]")
        self.bud_desc = page.get_by_text(re.compile("가입일(\\d+.\\d+.\\d+)부터 누적 금액 기준, 금액으로 환산 가능한 혜택만 포함"))

        self.on_hold_temparary_suspension_period = page.get_by_text(re.compile("\\d{4}.\\d{2}.\\d{2} ~ \\d{4}.\\d{2}.\\d{2}"))

        # coupang play benefit
        self.coupang_play_intro_image = page.locator("//div[contains(@class, 'PlayIntroVideo_swiper-container')]")

        # membership benefit lisst

        # CTA button
        self.cancellation_button = page.get_by_role("button", name="해지하기")

        # right-hand side bar
        self.promotion_banner_image_list = page.locator("//ul[@class='promotion-banner']/li/a/img").all()
        self.cart_count = page.locator("//div[@class='side-cart']")
        self.total_recently_viewed_count = page.locator("//div[@class='recently-viewed-products']")
        self.recently_viewed_product_section = page.locator("//div[@class='recently-viewed-list']")

        # Cancellation popup
        self.cancellation_popup_title = page.get_by_text("와우 멤버십 해지")
        cancellation_popup_frame = page.locator("iframe").nth(1)
        ## Step 1
        self.first_cancellation_page_calendar_img = cancellation_popup_frame.content_frame.get_by_role("img", name="달력 이미지")
        self.first_cancellation_page_remaining_days_text = cancellation_popup_frame.get_by_text(re.compile("이승훈님, 다음 결제일까지 아직 \\d+일 남았어요!"))
        self.first_cancellation_page_give_up_benefit_button = cancellation_popup_frame.content_frame.get_by_text("내가 받고 있는 혜택 포기하기")
        ## Step 2 (Survey)
        self.second_cancellation_survey_option_5 = cancellation_popup_frame.content_frame.locator("span").nth(4)
        self.second_cancellation_survey_option_5_textbox = cancellation_popup_frame.content_frame.get_by_role("textbox", name = "해지 이유를 적어주시면 서비스 개선에 많은 도움이 됩니다")
        self.second_cancellation_survey_cancellation_button = cancellation_popup_frame.content_frame.get_by_role("button", name="해지하기")
        ## Step 3
        self.third_cancellation_page_cancel_button = cancellation_popup_frame.content_frame.get_by_text("즉시 해지하기")

        # Confirmation popup
        self.confirmation_popup = page.locator("//div[contains(@class, 'alert_alert-popup-box')]")
        self.confirmation_popup_confirm_button = page.get_by_role("button", name =  "확인")

        ########### mobile web ###########
        ## Top GNB
        self.top_gnb_earch = page.locator("div#gnbBtnArea").locator("link#searchBtn")
        self.top_gnb_cart = page.locator("div#gnbBtnArea").locator("link#cartBtn")
        self.top_gnb_cart_count = page.locator("div#gnbBtnArea").locator("#gnbCartCnt")

        self.moweb_next_payment_date_text_area = page.locator("div#member-info-titleV2__date")
        self.moweb_next_payment_date_text = page.get_by_text(re.compile("다음 결제 예정일은 \\d+년 \\d+월 \\d+일 입니다"))

        self.wow_benefits_list = page.locator("//ul[contains@class, 'MembershipBenefits_benefits-container-mobile')\/li]").all()
        self.wow_benefits_last_item = page.locator("//ul[contains@class, 'MembershipBenefits_benefits-container-mobile')\/li]").nth(-1)

        ## Bottom GNB
        self.gnb_coupang_home = page.locator("nav#bottomMenu").get_by_role("link", name = "쿠팡홈")
        self.gnb_category = page.locator("nav#bottomMenu").get_by_role("link", name = "카테고리")
        self.gnb_search = page.locator("nav#bottomMenu").get_by_role("link", name = "검색")
        self.gnb_my_coupang = page.locator("nav#bottomMenu").get_by_role("link", name = "마이쿠팡")



    def click_signup_cta_button_on_wmp(self):
        self.signup_cta_button.click()

    def click_cancellation_cta_button_on_wmp(self):
        self.cancellation_button.click()

    def click_give_up_benefit_button_on_the_1st_cancellation_page(self):
        self.first_cancellation_page_give_up_benefit_button.click()
    
    def answer_the_survey_option_5(self, input_text = "test"):
        self.second_cancellation_survey_option_5.click()
        self.second_cancellation_survey_option_5_textbox.fill(input_text)

    def click_cancellation_button_on_the_cancellation_survey_page(self):
        self.second_cancellation_survey_cancellation_button.click()

    def click_cancellation_button_on_the_3rd_cancellation_page(self):
        self.third_cancellation_page_cancel_button.click()

    def click_confirm_button_on_the_confirmation_popup(self):
        self.confirmation_popup_confirm_button.click()




