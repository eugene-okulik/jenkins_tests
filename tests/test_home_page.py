from pages.home_page import HomePage
from time import sleep


def test_open_description_form(driver, start_session):
    sleep(5)
    home_page = HomePage(driver)
    home_page.open()
    home_page.description_link.click()
    assert home_page.description_area.is_displayed()
