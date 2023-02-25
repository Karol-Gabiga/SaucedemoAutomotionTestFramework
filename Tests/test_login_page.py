import pytest

from Utilities.BaseTest import BaseTest
from Utilities import Configuration
from PageObjects.LoginPage import LoginPage


class TestLogin(BaseTest):

    def test_page_title(self):
        login_page = LoginPage(self.driver)
        assert login_page.get_page_title(Configuration.PAGE_TITLE) == Configuration.PAGE_TITLE

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.insert_username(Configuration.VALID_USERNAME_1)
        login_page.insert_password(Configuration.VALID_PASSWORD)
        login_page.start_login()

