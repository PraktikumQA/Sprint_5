from selenium.webdriver.common.by import By
import time
from locators import Locators


def test_constructor_fillings_section(driver):

    driver.find_element(*Locators.FILLINGS_BUTTON).click()
    time.sleep(3)
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Краторная булка')]").is_displayed()
