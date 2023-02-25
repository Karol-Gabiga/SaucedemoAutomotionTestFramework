from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_locator = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_page_title(title)

    def insert_username(self, username):
        self.do_send_keys(LoginPage.username_locator, username)

    def insert_password(self, password):
        self.do_send_keys(LoginPage.password_locator, password)

    def start_login(self):
        self.do_click(LoginPage.login_locator)
