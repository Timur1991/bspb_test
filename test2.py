import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

"""
проверка запрета входа с невалидными учетными данными
"""

s = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)
print("C2211: Запрет входа с не валидными учетными данными")
try:
    driver.delete_all_cookies()
    driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

    rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    print(rand_string)
    username = driver.find_element(By.NAME, "username")
    username.clear()
    username.send_keys(rand_string)

    rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(rand_string)

    driver.find_element(By.ID, "login-button").click()
    if driver.find_element(By.ID, "login-button"): print ("\033[92m{}\033[0m".format("Test PASS"))
    driver.save_screenshot("screenshot_C2211.png")
except:
    driver.save_screenshot("Error_screenshot_C2211.png")
    print("\033[31m{}\033[0m".format("Test FAIL"))
driver.quit()