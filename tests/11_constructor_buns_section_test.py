from locators import Locators


def test_constructor_buns_section(driver):
    driver.find_element(*Locators.FILLINGS_BUTTON).click()
    driver.find_element(*Locators.BUNS_BUTTON).click()
    buns_class = driver.find_element(*Locators.BUNS_BUTTON).get_attribute('class')
    assert 'current' in buns_class
