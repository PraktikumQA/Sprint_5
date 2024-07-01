from selenium.webdriver.common.by import By

from locators import Locators


def test_registration_with_invalid_password(driver):
    name = "Test19User"
    email = "319@ya.ru"
    password = "123"
    driver.find_element(*Locators.AUTH_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTRATION_CONFORMATION_BUTTON).click()

    error_message = driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")
    assert error_message.is_displayed()