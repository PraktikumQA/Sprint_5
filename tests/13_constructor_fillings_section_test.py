from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_constructor_fillings_section(driver):
    driver.find_element(*Locators.FILLINGS_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLINGS_TITLE))

    assert driver.find_element(*Locators.FILLINGS_TITLE).is_displayed()
