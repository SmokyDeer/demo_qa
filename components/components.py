from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement

class WebElement:
    def __init__(self, driver, locator = ''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self) -> SeleniumWebElement:
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True