__author__ = 'Proyecto'


from selenium.webdriver.common.by import By


class AddNewFunctionaryLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    HEADER = (By.XPATH, "//div[@class='page-header']/h1")
    FIRST_NAME_INPUT = (By.ID, "firstname")
    FIRST_SURNAME_INPUT = (By.ID, "firstsurname")
    SECOND_SURNAME_INPUT = (By.ID, "secondsurname")
    IDENTIFICATION_INPUT = (By.ID, "identification")
    BIRTHDATE_INPUT = (By.ID, "birthdate")
    MARITAL_STATUS_COMBO = (By.ID, "maritalstatus")
    ADDRESS_INPUT = (By.ID, "address")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_NUMBER_INPUT = (By.ID, "phonenumber")
    CELLPHONE_NUMBER = (By.ID, "cellphonenumber")
    ROLE_COMBO = (By.ID, "role")
    HIRE_DATE_INPUT = (By.ID, "hiredate")
    STATUS_COMBO = (By.ID, "status")
    SAVE_FUNCTIONARY_RESUME_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[2]/input")
    ADD_NEW_FUNCTIONARY_ERROR_MSG = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[3]/strong")



class AddNewFunctionaryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(CreateStudentLocators.TITLE, 30)

    def enter_first_name(self, first_name):
        self.driver.send_keys(AddNewFunctionaryLocators.FIRST_NAME_INPUT[0], AddNewFunctionaryLocators.FIRST_NAME_INPUT[1], first_name)

    def enter_first_surname(self, first_surname):
        self.driver.send_keys(AddNewFunctionaryLocators.FIRST_NAME_INPUT[0], AddNewFunctionaryLocators.FIRST_NAME_INPUT[1], first_surname)

    def enter_second_surname(self, second_surname):
        self.driver.send_keys(AddNewFunctionaryLocators.SECOND_SURNAME_INPUT[0], AddNewFunctionaryLocators.SECOND_SURNAME_INPUT[1], second_surname)

    def enter_identification(self, identification):
        self.driver.send_keys(AddNewFunctionaryLocators.IDENTIFICATION_INPUT[0], AddNewFunctionaryLocators.IDENTIFICATION_INPUT[1], identification)

    def enter_birthdate(self, birthdate):
        self.driver.send_keys(AddNewFunctionaryLocators.BIRTHDATE_INPUT[0], AddNewFunctionaryLocators.BIRTHDATE_INPUT[1], birthdate)

    def enter_address(self, address):
        self.driver.send_keys(AddNewFunctionaryLocators.ADDRESS_INPUT[0], AddNewFunctionaryLocators.ADDRESS_INPUT[1], address)

    def enter_phone_number(self, phone_number):
        self.driver.send_keys(AddNewFunctionaryLocators.PHONE_NUMBER_INPUT[0], AddNewFunctionaryLocators.PHONE_NUMBER_INPUT[1], phone_number)

    def enter_cellphone_number(self, cellphone_number):
        self.driver.send_keys(AddNewFunctionaryLocators.CELLPHONE_NUMBER[0], AddNewFunctionaryLocators.CELLPHONE_NUMBER[1], cellphone_number)

    def enter_hire_date(self, hire_date):
        self.driver.send_keys(AddNewFunctionaryLocators.HIRE_DATE_INPUT[0], AddNewFunctionaryLocators.HIRE_DATE_INPUT[1], hire_date)

    def enter_email(self, email):
        self.driver.send_keys(AddNewFunctionaryLocators.EMAIL[0], AddNewFunctionaryLocators.EMAIL[1], email)

    def select_marital_status(self, marital_status):
        self.driver.set_combo_option(AddNewFunctionaryPage.MARITAL_STATUS_COMBO[0], AddNewFunctionaryLocators.MARITAL_STATUS_COMBO[1], marital_status)

    def select_role(self, role):
        self.driver.set_combo_option(AddNewFunctionaryPage.ROLE_COMBO[0], AddNewFunctionaryLocators.ROLE_COMBO[1], role)

    def select_status(self, status):
        self.driver.set_status(AddNewFunctionaryPage.STATUS_COMBO[0], AddNewFunctionaryPage.STATUS_COMBO[1], status)

    def click_save_button(self):
        self.driver.click(AddNewFunctionaryPage.click_save_button[0], AddNewFunctionaryPage.click_save_button[1])

    def is_save_new_functionary_error_message_display(self):
        return self.driver.wait_for_element_visible(AddNewFunctionaryLocators.ADD_NEW_FUNCTIONARY_ERROR_MSG[0], AddNewFunctionaryLocators.ADD_NEW_FUNCTIONARY_ERROR_MSG[1], 30)




