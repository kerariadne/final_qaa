import pytest
from actions import get_random_user_data, Actions
from selenium import webdriver
from locators import RegistrationFormLocators

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def actions(driver):
    actions = Actions(driver)
    return actions

def test_registration_form(actions):
    user_data = get_random_user_data()
    actions.fill_registration_form(user_data)
    assert user_data is not None, "User data should not be None"

def test_negative_registration_form(actions):
    user_data = get_random_user_data()
    user_data["login"]["password"] = ""
    actions.fill_registration_form(user_data)
    error_message = actions.driver.find_element(*RegistrationFormLocators.ERROR_MESSAGE_ELEMENT).text
    assert error_message == "Password is required."


if __name__ == "__main__":
    pytest.main()
