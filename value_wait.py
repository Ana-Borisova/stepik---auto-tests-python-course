from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    value = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = int(browser.find_element_by_id('input_value').text)
    y = calc(x_element)
    answer = browser.find_element_by_class_name('form-control')
    answer.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
