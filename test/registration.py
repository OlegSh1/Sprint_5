from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_email, get_correctPassword, get_name, get_uncorrectPasswort
import pytest

def test_registration(get_name, get_email, get_correctPassword):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH,".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button[text()='Войти в аккаунт']").click()

    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(get_name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(get_email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(get_correctPassword)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 3).until((expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']"))))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()

def test_uncorrect_password(get_name, get_email, get_uncorrectPasswort):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH,".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button[text()='Войти в аккаунт']").click()

    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(get_name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(get_email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(get_uncorrectPasswort)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']") != 0

    driver.quit()