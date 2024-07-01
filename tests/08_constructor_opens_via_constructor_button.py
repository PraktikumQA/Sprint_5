from selenium.webdriver.common.by import By

from locators import Locators


def test_constructor_opens_via_constructor_button(driver):
    email = "av317@ya.ru"
    password = "av7%17"
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").is_displayed()