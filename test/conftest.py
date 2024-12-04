import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL_HOME_PAGE)
    yield browser
    browser.quit()