from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_autorization_on_main():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('oleg.shadrikov123@gmail.com')
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_autorization_on_account():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('oleg.shadrikov123@gmail.com')
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_autorization_on_register():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('oleg.shadrikov123@gmail.com')
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_autorization_on_forgot_password():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('oleg.shadrikov123@gmail.com')
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()