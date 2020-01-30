from selenium import webdriver
import time
import math

try:
     browser = webdriver.Chrome()
     browser.get("http://suninjuly.github.io/execute_script.html")
     def calc(x):
         return str(math.log(abs(12*math.sin(int(x)))))
     x_element = int(browser.find_element_by_id('input_value').text)
     y = calc(x_element)
     browser.execute_script("window.scrollBy(0, 10);")
     answer = browser.find_element_by_class_name('form-control')
     answer.send_keys(y)
     option1 = browser.find_element_by_id('robotCheckbox')
     option1.click()
     option2 = browser.find_element_by_id('robotsRule')
     browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
     option2.click()
     button = browser.find_element_by_css_selector("button.btn")
     button.click()
finally:
     time.sleep(10)
     browser.quit()