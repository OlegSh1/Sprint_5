from Locators import Locators

class TestMoveInConstructor:
    def test_move_on_buns(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()
        assert driver.find_element(*Locators.BUNS).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_move_on_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        assert driver.find_element(*Locators.SAUCES).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_move_on_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert driver.find_element(*Locators.FILLINGS).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'