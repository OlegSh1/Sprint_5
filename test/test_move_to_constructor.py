from Locators import Locators
from constants import Constants

class TestMoveToConstructor:
    def test_move_to_constructor(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        assert driver.current_url == Constants.URL_HOME_PAGE

    def test_move_to_constructor_logo(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == Constants.URL_HOME_PAGE