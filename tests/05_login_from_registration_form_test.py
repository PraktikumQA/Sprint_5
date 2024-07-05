from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants

from locators import Locators

def test_login_from_registration_form(driver):
    driver.find_element(*Locators.AUTH_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    driver.find_element(*Locators.LOGIN_FROM_AUTH_FORM_BUTTON).click()
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL_MAIN_PAGE))
    assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()
