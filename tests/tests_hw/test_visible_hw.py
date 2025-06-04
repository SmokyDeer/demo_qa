from pages.accordion import AccordionPage
import time

def test_visible_accordion(browser):
    accordion_page = AccordionPage(browser)
    accordion_page.visit()

    assert accordion_page.section1_content.find_element().is_displayed()

    accordion_page.section1_heading.click()
    time.sleep(2)
    assert not accordion_page.section1_content.find_element().is_displayed()

def test_visible_accordion_default(browser):
    accordion_page = AccordionPage(browser)
    accordion_page.visit()

    assert not accordion_page.section2_content_p1.find_element().is_displayed()
    assert not accordion_page.section2_content_p2.find_element().is_displayed()
    assert not accordion_page.section3_content.find_element().is_displayed()