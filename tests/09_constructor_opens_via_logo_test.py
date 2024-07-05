from constants import Constants

from locators import Locators


def test_constructor_opens_via_logo(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGO).click()
    assert driver.find_element(*Locators.CONSTRUCTOR_TITLE).is_displayed()
