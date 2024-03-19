from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.ID, 'num1')
    value2 = browser.find_element(By.ID, 'num2')

    res = int(value1.text) + int(value2.text)

    # browser.find_element(By.TAG_NAME, "select").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(3)
    browser.quit()
