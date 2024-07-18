import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationFormLocators

def get_random_user_data():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    return data["results"][0]

class Actions:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, user_data):
        self.driver.get("https://parabank.parasoft.com/parabank/register.htm")
        self.driver.find_element(*RegistrationFormLocators.FIRST_NAME_INPUT).send_keys(user_data["name"]["first"])
        self.driver.find_element(*RegistrationFormLocators.LAST_NAME_INPUT).send_keys(user_data["name"]["last"])
        self.driver.find_element(*RegistrationFormLocators.ADDRESS_INPUT).send_keys(user_data["location"]["street"]["name"])
        self.driver.find_element(*RegistrationFormLocators.CITY_INPUT).send_keys(user_data["location"]["city"])
        self.driver.find_element(*RegistrationFormLocators.STATE_INPUT).send_keys(user_data["location"]["state"])
        self.driver.find_element(*RegistrationFormLocators.ZIP_CODE_INPUT).send_keys(user_data["location"]["postcode"])
        self.driver.find_element(*RegistrationFormLocators.PHONE_INPUT).send_keys(user_data["phone"])
        self.driver.find_element(*RegistrationFormLocators.SSN_INPUT).send_keys(user_data["id"]["value"])
        self.driver.find_element(*RegistrationFormLocators.USERNAME_INPUT).send_keys(user_data["login"]["username"])
        self.driver.find_element(*RegistrationFormLocators.PASSWORD_INPUT).send_keys(user_data["login"]["password"])
        self.driver.find_element(*RegistrationFormLocators.CONFIRM_PASSWORD_INPUT).send_keys(user_data["login"]["password"])
        self.driver.find_element(*RegistrationFormLocators.REGISTER_BUTTON).click()
