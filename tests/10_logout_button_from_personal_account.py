from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_logout_button_from_personal_account(driver):
    email = "av317@ya.ru"
    password = "av7%17"
    driver.find_element(*Locators.AUTH_BUTTON).click()
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    assert driver.find_element(By.XPATH, "//div[contains(@class,'Auth_login__3hAey')]").is_displayed()
