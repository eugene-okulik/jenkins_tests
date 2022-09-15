import pytest
from selenium import webdriver
from pages.login_page import LoginPage


USERNAME = 'user1'
PASSWORD = '1password1'


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def start_session(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.log_in(USERNAME, PASSWORD)
    yield None
