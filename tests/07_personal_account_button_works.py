from selenium.webdriver.common.by import By

from locators import Locators


def test_personal_account_button_works(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed()