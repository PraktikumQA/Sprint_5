from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_login_from_home_page(driver):
    email = "av317@ya.ru"
    password = "av7%17"
    driver.find_element(*Locators.AUTH_BUTTON).click()
    driver.find_element(*Locators.AUTH_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.AUTH_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
    assert driver.find_element(By.XPATH, "//a[contains(text(),'Профиль')]").is_displayed()
