from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_logout_button_from_personal_account(login):
    driver = login
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()
