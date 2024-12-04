from Locators import Locators
from constants import Constants


class TestMoveToPersonalAccount:
    def test_move_to_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert driver.current_url == Constants.URL_AUTORIZATION_PAGE