from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.submenu_items = WebElement(driver, 'div.element-list.collapse.show > ul > li')
        self.main_page_icon = WebElement(driver, '#app > header > a')