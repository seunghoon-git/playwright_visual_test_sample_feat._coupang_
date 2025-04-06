import time
import re

class WowMembershipCancellationPopup1:
    def __init__(self, page):
        self.page = page
        self.calendar_img = page.get_by_role("img", name="달력 이미지")
        self.remaining_days_text = page.locator("//div[contains(@class, 'NoticeMessage_nebefit-notice__message_content')]")
        self.benefit_play_carousel = page.locator("//div[contains(@class, 'benefit_play-carousel)]")
        self.give_up_benefit_button = page.locator("내가 받고 있는 혜택 포기하기")

class WowMembershipCancellationPopup2:
    def __init__(self, page):
        self.page = page
        self.survey_option_5 = page.locator("span").nth(4)
        self.survey_option_5_textbox = page.get_by_role("textbox", name="해지 이유를 적어주시면 서비스 개선에 많은 도움이 됩니다")
        self.survey_cancellation_button = page.get_by_role("button", name="해지하기")

class WowMembershipCancellationPoupup3:
    def __init__(self, page):
        self.page = page
        self.cancel_button = page.get_by_text("즉시 해지하기")

class WowMembershipCancellationConfirmationPopup:
    def __init__(self, page):
        self.page = page
        self.confirmation_popup = page.locator("//div[contains(@class, 'alert_alert-popup-box')]")
        self.confirmation_popup_confirm_button = page.get_by_role("button", Name="확인")
