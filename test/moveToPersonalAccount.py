from selenium import webdriver
from selenium.webdriver.common.by import By

def test_moveToPersonalAccount():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, ".//a[@href='/account']").click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()