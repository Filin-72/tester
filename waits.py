from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "100"
                                         ))
    button = browser.find_element_by_xpath('//*[@id="book"]')
    button.click()

    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x_element2 = x_element.text
    y = calc(int(x_element2))
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)
    button2 = browser.find_element_by_xpath('//*[@id="solve"]')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()



