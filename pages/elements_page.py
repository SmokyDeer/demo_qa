from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.please_select_text = WebElement(driver,"//div[contains(text(), 'Please select an item from left to start practice.')]",  by=By.XPATH)

