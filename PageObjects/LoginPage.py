from selenium.webdriver.common.by import By


class LoginPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title()