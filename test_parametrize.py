import pytest
from selenium import webdriver
import math
import time

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()
@pytest.mark.parametrize('links',
["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_link(browser, links):
    link = f"{links}/"
    browser.get(link)
    area = browser.find_element_by_css_selector('.textarea')
    answer = math.log(int(time.time()))
    area.send_keys(str(answer))
    button = browser.find_element_by_class_name('submit-submission').click()
    message = browser.find_element_by_css_selector('.smart-hints__hint').text
    assert message == "Correct!", "It's not correct"
