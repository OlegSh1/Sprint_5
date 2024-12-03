from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_exitPersonalAcount():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('oleg.shadrikov123@gmail.com')
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    driver.find_element(By.XPATH, ".//a[@href='/account']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//ul/li[3]/button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")))
    driver.find_element(By.XPATH, ".//ul/li[3]/button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()