from locators import Locators


def test_constructor_fillings_section(driver):
    driver.find_element(*Locators.FILLINGS_BUTTON).click()
    fillings_class = driver.find_element(*Locators.FILLINGS_BUTTON).get_attribute('class')
    assert 'current' in fillings_class
