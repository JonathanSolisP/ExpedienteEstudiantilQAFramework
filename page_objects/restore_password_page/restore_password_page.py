__author__ = 'Proyecto'


from selenium.webdriver.common.by import By

__author__ = 'Proyecto'



class RestorePasswordLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    USERNAME_INPUT = (By.ID, "username")
    SUBMIT_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div/form/fieldset/div[2]/button")
    SUBMIT_USERNAME_ERROR_MSG = (By.XPATH, "/html/body/section/section/section/section/div/form/fieldset/div[3]/strong")


class RestorePasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(RestorePasswordLocators.TITLE, 30)

    def enter_username(self, username):
        self.driver.send_keys(RestorePasswordLocators.USERNAME_INPUT[0], RestorePasswordLocators.USERNAME_INPUT[1], username)

    def click_submit_button(self):
        self.driver.click(*RestorePasswordLocators.SUBMIT_BUTTON)

    def is_submit_username_error_displayed(self):
        return self.driver.wait_for_element_visible(RestorePasswordLocators.SUBMIT_USERNAME_ERROR_MSG[0], RestorePasswordLocators.SUBMIT_USERNAME_ERROR_MSG[1], 30)

