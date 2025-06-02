from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement

class WebElement:
    def __init__(self, driver, locator = '', by=By.CSS_SELECTOR):
        self.driver = driver
        self.locator = locator
        self.by = by

    def click(self): #клик по чему либо
        self.find_element().click()

    def find_element(self) -> SeleniumWebElement: #найти элемент
        return self.driver.find_element(self.by, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)