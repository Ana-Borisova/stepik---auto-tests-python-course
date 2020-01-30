from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = int(browser.find_element_by_id('input_value').text)
    y = calc(x_element)
    answer = browser.find_element_by_class_name('form-control')
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
