import pytest

from selenium import webdriver
from Utilities import Configuration


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )


@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def setup(request, cmdopt):
    browser = cmdopt
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    driver.get(Configuration.TEST_PAGE)
    request.cls.driver = driver
    yield
    driver.close()
