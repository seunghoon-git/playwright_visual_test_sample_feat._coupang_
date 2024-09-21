import time

class LoginPage:  
    def __init_(self, page):  
        self.page = page
        self.email_login_tab = page.get_by_role("link", name = "이메일 로그인")
        self.phone_number_login_tab = page.get_by_role("link", name = "휴대폰번호 로그인")
        self.qr_login_tab = page.get_by_role("link", name="QR코드 로그인")
        self.qr_login_number = page.locator(".qr-login__number")
        self.qr_login_image = page.locator(".qr-login__image")
        self.qr_login_timer = page.locator(".qr-login__timer")

    
    
    def select_email_login(self):
        self.email_login_tab.click()
        time.sleep(1)

    
    def select_phone_number_login(self):
        self.phone_number_login_tab.click()
        time.sleep(1)

    
    def select_qr_login(self):
        self.qr_login_tab.click()
        time.sleep(1)
