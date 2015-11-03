from selenium.webdriver.common.by import By



__author__ = 'Proyecto'



class SignUpLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    USERNAME_INPUT = (By.XPATH, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SIGN_UP_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[6]/button")
    SIGN_UP_ERROR_MSG = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[7]")

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(SignUpLocators.TITLE, 30)

    def enter_first_name(self, first_name):
        self.driver.send_keys(SignUpLocators.FIRSTNAME_INPUT[0], SignUpLocators.FIRSTNAME_INPUT[1], first_name)

    def enter_last_name(self, last_name):
        self.driver.send_keys(SignUpLocators.LASTNAME_INPUT[0], SignUpLocators.LASTNAME_INPUT[1], last_name)

    def enter_email(self, email):
        self.driver.send_keys(SignUpLocators.EMAIL_INPUT[0], SignUpLocators.EMAIL_INPUT[1], email)

    def enter_username(self, username):
        self.driver.send_keys(SignUpLocators.USERNAME_INPUT[0], SignUpLocators.USERNAME_INPUT[1], username)

    def enter_password(self, password):
        self.driver.send_keys(SignUpLocators.PASSWORD_INPUT[0], SignUpLocators.PASSWORD_INPUT[1], password)

    def click_sign_up_button(self):
        self.driver.click(*SignUpLocators.SIGN_UP_BUTTON)

    def is_sign_up_error_message_display(self):
        return self.driver.wait_for_element_visible(SignUpLocators.SIGN_UP_ERROR_MSG[0], SignUpLocators.SIGN_UP_ERROR_MSG[1], 30)
