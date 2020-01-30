from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = int(browser.find_element_by_id('input_value').text)
    y = calc(x_element)
    answer = browser.find_element_by_class_name('form-control')
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
