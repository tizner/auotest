# Выпадающий  список

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = int(x_element1.text)

    x_element2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = int(x_element2.text)

    y = str(x1 + x2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()