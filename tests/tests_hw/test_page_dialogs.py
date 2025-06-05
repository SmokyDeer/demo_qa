from pages.modal_dialogs import ModalDialogsPage
import time

def test_madal_elements(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.submenu_items.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    modal_dialogs_page.refresh()
    modal_dialogs_page.main_page_icon.click()
    browser.back()
    browser.set_window_size(900,400)
    browser.forward()

    time.sleep(2)
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == "DEMOQA"

    browser.set_window_size(1000, 1000)