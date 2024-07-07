from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker

from constants import Constants

from locators import Locators

faker = Faker()

class Test_reg_suc:
    def test_registration_successful(self, driver):
        name = faker.name()
        email = faker.email()
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTRATION_CONFORMATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL_AUTHORIZATION_PAGE))
        driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL_MAIN_PAGE))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()
