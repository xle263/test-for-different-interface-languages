import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome('c:/chromedriver.exe')
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_css_selector("button.btn").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    y = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(y))

    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
