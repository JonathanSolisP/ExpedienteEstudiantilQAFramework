from selenium.webdriver.common.by import By


class CreateStudentLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    NAME_INPUT = (By.ID, "name")
    FIRST_LAST_NAME_INPUT = (By.ID, "primer_apellido")
    SECOND_LAST_NAME_INPUT = (By.ID, "segundo_apellido")



class CreateStudentPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(CreateStudentLocators.TITLE, 30)

    def enter_name(self, name):
        self.driver.send_keys(CreateStudentLocators.NAME_INPUT[0], CreateStudentLocators.NAME_INPUT[1], name)

    def enter_first_last_name(self, first_last_name):
        self.driver.send_keys(CreateStudentLocators.FIRST_LAST_NAME_INPUT[0], CreateStudentLocators.FIRST_LAST_NAME_INPUT[1], first_last_name)

    def enter_second_last_name(self, second_last_name):
        self.driver.send_keys(CreateStudentLocators.SECOND_LAST_NAME_INPUT[0], CreateStudentLocators.SECOND_LAST_NAME_INPUT[1], second_last_name)

