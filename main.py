import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

"""
Добавление номера телефона на определенную карту для оплаты в интернете на вкладке "Карты"
"""


def run_selenium(url):
    s = Service('C:/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    try:
        driver.set_window_size(1920, 1080)
        driver.get(url=url)
        driver.find_element(By.ID, 'login-button').click()  # входим в аккаунт бспб
        time.sleep(1)
        driver.find_element(By.ID, 'login-otp-button').click()  # подтверждаем двухфакторную авторизацию
        time.sleep(1)
        driver.find_element(By.ID, 'cards-overview-index').click()  # переходим на вкладку "Карты"
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,'Оплата в интернете').click()  # переходим на вкладку "оплата в интернете"
        time.sleep(1)
        # driver.find_element(By.NAME, "phoneNumber").click()
        driver.find_element(By.NAME, "phoneNumber").clear()  # очищаем поле ввода номера телефона
        driver.find_element(By.NAME, "phoneNumber").send_keys('+79999999999')  # отправляем номер телефона
        driver.find_element(By.ID, "add-card-notification").click()  # жмем подтвердить
        time.sleep(2)
        driver.switch_to.frame(0)  # переключаем на модальное окно подтверждения
        driver.find_element(By.ID, 'otp-input').clear()  # очищаем поле для ввода кода с смс
        driver.find_element(By.ID, 'otp-input').send_keys('0000')  # вводим код из смс
        driver.find_element(By.ID, "confirm").click()  # ждмем кнопку "подтвердить"
        time.sleep(3)
        driver.save_screenshot('test_success.png')  # делаем скрин успешного добавления телефона для интернет оплаты
        print('Тест пройден успешно. Скриншот сохранен!')
    except Exception as ex:
        print(f'Ошибка: {ex}')
        driver.quit()


if __name__ == '__main__':
    run_selenium('https://idemo.bspb.ru/')

