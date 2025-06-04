from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.common.by import By


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    actual_footer_text = demo_qa_page.footer.get_text()
    expented_footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    assert actual_footer_text == expented_footer_text

def test_check_elements_page_text(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.button_elenents.click()

    actual_center_text = element_page.please_select_text.get_text()
    expected_center_text = 'Please select an item from left to start practice.'

    assert actual_center_text == expected_center_text

# def test_page_elements(browser):
#     el_page = ElementsPage(browser)
#
#     el_page.visit()