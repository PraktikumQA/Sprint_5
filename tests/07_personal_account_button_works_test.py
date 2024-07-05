from locators import Locators


def test_personal_account_button_works(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()
