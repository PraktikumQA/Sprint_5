from selenium.webdriver.common.by import By
import time
from locators import Locators


def test_constructor_sauces_section(driver):
    driver.find_element(*Locators.SAUCES_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Соус традиционный галактический')]").is_displayed()
