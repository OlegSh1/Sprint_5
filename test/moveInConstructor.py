import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_moveOnBuns():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[text()='Булки']/parent::div")))
    driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::div").click()

    assert driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    driver.quit()
def test_moveOnSauces():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").click()

    assert driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    driver.quit()

def test_moveOnFillings():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, ".//span[text()='Начинки']/parent::div").click()

    assert driver.find_element(By.XPATH, ".//span[text()='Начинки']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    driver.quit()