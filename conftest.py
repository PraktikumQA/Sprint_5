import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import Constants

from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get(Constants.URL_MAIN_PAGE)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.get(Constants.URL_AUTHORIZATION_PAGE)
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver