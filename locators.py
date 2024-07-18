from selenium.webdriver.common.by import By

class RegistrationFormLocators:
    FIRST_NAME_INPUT = (By.ID, "customer.firstName")
    LAST_NAME_INPUT = (By.ID, "customer.lastName")
    ADDRESS_INPUT = (By.ID, "customer.address.street")
    CITY_INPUT = (By.ID, "customer.address.city")
    STATE_INPUT = (By.ID, "customer.address.state")
    ZIP_CODE_INPUT = (By.ID, "customer.address.zipCode")
    PHONE_INPUT = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[7]/td[2]/input")
    SSN_INPUT = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[8]/td[2]/input")
    USERNAME_INPUT = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[10]/td[2]/input")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[11]/td[2]/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[12]/td[2]/input")
    REGISTER_BUTTON = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input")
    ERROR_MESSAGE_ELEMENT = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[11]/td[3]/span")
    ERROR_MESSAGE_ELEMENT1 = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[10]/td[3]/span")
