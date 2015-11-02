from selenium.webdriver.common.by import By

__author__ = 'Proyecto'



class LoginLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SIGN_IN_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[3]/button")
    SIGN_IN_ERROR_MSG = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[5]/strong")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(LoginLocators.TITLE, 30)

    def enter_username(self, username):
        self.driver.send_keys(LoginLocators.USERNAME_INPUT[0], LoginLocators.USERNAME_INPUT[1], username)

    def enter_password(self, password):
        self.driver.send_keys(LoginLocators.PASSWORD_INPUT[0], LoginLocators.PASSWORD_INPUT[1], password)

    def click_sign_in_button(self):
        self.driver.click(*LoginLocators.SIGN_IN_BUTTON)

    def is_sign_in_error_message_displayed(self):
        return self.driver.wait_for_element_visible(LoginLocators.SIGN_IN_ERROR_MSG[0], LoginLocators.SIGN_IN_ERROR_MSG[1], 30)
