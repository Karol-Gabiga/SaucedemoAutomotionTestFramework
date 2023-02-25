from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text_from_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_enabled(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return bool(element)

    def verify_link_presence(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def get_page_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title
