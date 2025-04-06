import time

class LoginPage:  
    def __init__(self, page):  
        self.page = page
        self.email_login_tab = page.get_by_role("link", name = "이메일 로그인")
        self.phone_number_login_tab = page.get_by_role("link", name = "휴대폰번호 로그인")
        self.qr_login_tab = page.get_by_role("link", name="QR코드 로그인")
        self.qr_login_number = page.locator(".qr-login__number")
        self.qr_login_image = page.locator(".qr-login__image")
        self.qr_login_timer = page.locator(".qr-login__timer")
        self.email_input_field = page.locator("#login-email-input")
        self.password_input_field = page.locator("#login-password-input")
        self.login_button = page.get_by_role("button", name="로그인")

    
    
    def select_email_login(self):
        self.email_login_tab.click()
        time.sleep(1)

    
    def select_phone_number_login(self):
        self.phone_number_login_tab.click()
        time.sleep(1)

    
    def select_qr_login(self):
        self.qr_login_tab.click()
        time.sleep(1)


    def type_email_field(self, email):
        self.email_input_field.type(email)


    def type_password_field(self, password):
        self.password_input_field.type(password)
    
    
    def login_with_email(self, email, password, redirect_url = None):
        from pages.GateWay import GateWay

        self.type_email_field(email)
        self.type_password_field(password)
        self.login_button.click()
        self.page.wait_for_load_state("load")
        time.sleep(3)
        if redirect_url:
            self.page.goto(redirect_url)
            time.sleep(3)
            