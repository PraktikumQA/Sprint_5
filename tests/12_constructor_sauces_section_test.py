from locators import Locators


def test_constructor_sauces_section(driver):
    driver.find_element(*Locators.SAUCES_BUTTON).click()
    sauces_class = driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')
    assert 'current' in sauces_class
