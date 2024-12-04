from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators
from constants import Constants


class TestAutorization:
    def test_autorization_on_main(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER))
        assert driver.current_url == Constants.URL_HOME_PAGE


    def test_autorization_on_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER))
        assert driver.current_url == Constants.URL_HOME_PAGE

    def test_autorization_on_register(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.LOGIN_BUTTON_IN_PAGE_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER))
        assert driver.current_url == Constants.URL_HOME_PAGE

    def test_autorization_on_forgot_password(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_FORGOT_PASSWORD).click()
        driver.find_element(*Locators.LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER))
        assert driver.current_url == Constants.URL_HOME_PAGE