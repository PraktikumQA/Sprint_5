from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker

from constants import Constants

from locators import Locators

faker = Faker()


def test_registration_with_invalid_password(driver):
    name = faker.name()
    email = faker.email()
    driver.find_element(*Locators.AUTH_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(Constants.PASSWORD_WRONG)
    driver.find_element(*Locators.REGISTRATION_CONFORMATION_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_MESSAGE_WRONG_PASSWORD))
    error_message = driver.find_element(*Locators.REGISTRATION_MESSAGE_WRONG_PASSWORD)
    assert error_message.is_displayed()
