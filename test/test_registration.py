from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators
from helpers import get_name, get_email, get_correctPassword
from constants import Constants
from helpers import get_uncorrectPasswort


class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.NAME_IN_REGISTRATION).send_keys(get_name())
        driver.find_element(*Locators.EMAIL_IN_REGISTRATION).send_keys(get_email())
        driver.find_element(*Locators.PASSWORD_IN_REGISTRATION).send_keys(get_correctPassword())
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 3).until((expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']"))))

        assert driver.current_url == Constants.URL_AUTORIZATION_PAGE

    def test_uncorrect_password(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.NAME_IN_REGISTRATION).send_keys(get_name())
        driver.find_element(*Locators.EMAIL_IN_REGISTRATION).send_keys(get_email())
        driver.find_element(*Locators.PASSWORD_IN_REGISTRATION).send_keys(get_uncorrectPasswort())
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        assert driver.current_url == Constants.URL_REGISTRATION_PAGE