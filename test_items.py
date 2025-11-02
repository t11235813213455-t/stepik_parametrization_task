from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_be_add_to_basket_button(browser):
    browser.get(link)
    wait = WebDriverWait(browser, 10)
    try:
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
        assert add_to_basket_button is not None
    except NoSuchElementException:
        assert False, "Button add to basket not found"
    time.sleep(5)
