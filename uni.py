import unittest
from selenium import webdriver
import time

class Test12(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_css_selector("div.first_block input.first").send_keys("Ivan")
        browser.find_element_by_css_selector("div.first_block input.second").send_keys("Petrov")
        browser.find_element_by_css_selector("div.first_block input.third").send_keys("test@test.com")

        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        self.assertEqual(('h1.text'), 'h1.text', "Congratulations! You have successfully registered!")
        time.sleep(5)
        browser.quit()
    def test_2(self1):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_css_selector("div.first_block input.first").send_keys("Ivan")
        browser.find_element_by_css_selector("div.first_block input.second").send_keys("Petrov")
        browser.find_element_by_css_selector("div.first_block input.third").send_keys("test@test.com")

        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(5)
        self.assertEqual(('h1.text'), 'h1.text', "Congratulations! You have successfully registered!")
        time.sleep(5)
        browser.quit()
if __name__ == "__main__":
    unittest.main()
