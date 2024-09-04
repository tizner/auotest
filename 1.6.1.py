from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")

    time.sleep(3)

    button.click()

    time.sleep(3)
# закрываем браузер после всех манипуляций
finally:
    browser.quit()