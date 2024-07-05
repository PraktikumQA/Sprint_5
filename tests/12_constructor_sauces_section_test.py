from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_constructor_sauces_section(driver):
    driver.find_element(*Locators.SAUCES_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCES_TITLE))
    assert driver.find_element(*Locators.SAUCES_TITLE).is_displayed()
