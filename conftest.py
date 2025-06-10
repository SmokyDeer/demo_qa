import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.set_window_size(width=1000, height=1000)
        yield driver
    finally:
        if driver:
            driver.quit()