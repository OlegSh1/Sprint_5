from selenium import webdriver
from selenium.webdriver.common.by import By

def test_moveToConstructor():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']").click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_moveToConstructor_logotip():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']").click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()