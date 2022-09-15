from pages.base_page import BasePage
from selenium.webdriver.common.by import By


description_link = (By.ID, 'description-link')
description_area = (By.CSS_SELECTOR, 'textarea[name="description"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def description_link(self):
        return self.find_element(description_link)

    @property
    def description_area(self):
        return self.find_element(description_area)

    def open(self):
        self.driver.get('http://164.92.136.89:8080/')
