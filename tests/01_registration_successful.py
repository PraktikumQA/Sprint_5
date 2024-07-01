from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_registration_successful(driver):
    name = "Test29User"
    email = "av329@ya.ru"
    password = "av7%29"
    driver.find_element(*Locators.AUTH_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTRATION_CONFORMATION_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
    assert driver.find_element(By.XPATH, "//a[contains(text(),'Профиль')]").is_displayed()
