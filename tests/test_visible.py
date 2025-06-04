import time

from pages.elements_page import ElementsPage

def test_visible_btn_sidebar(browser):
    elenents_page = ElementsPage(browser)

    elenents_page.visit()
    assert elenents_page.button_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elenents_page = ElementsPage(browser)

    elenents_page.visit()
    assert elenents_page.button_sidebar_first_checkbox.visible()

    elenents_page.button_sidebar_first.click()
    time.sleep(2)
    assert not elenents_page.button_sidebar_first_checkbox.visible()