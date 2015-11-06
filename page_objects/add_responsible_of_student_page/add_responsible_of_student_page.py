from selenium.webdriver.common.by import By
from base.base_test import BaseTest

__author__ = 'Proyecto'


class AddResponsibleOfStudentLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    PAGE_HEADER = (By.XPATH, "/html/body/section/section/section/section/div[1]/h1")
    FIRST_NAME = (By.ID, "name")
    FIRST_SURNAME = (By.ID, "primer_apellido")
    SECOND_SURNAME = (By.ID, "segundo_apellido")
    IDENTIFICATION = (By.ID, "cedula")
    RELATIONSHIP = (By.ID, "parentesco")
    JOB = (By.ID, "ocupacion")
    MARITAL_STATUS = (By.ID, "estado_civil")
    NATIONALITY = (By.ID, "nacionalidad")
    PHONE_NUMBER = (By.ID, "telefono")
    EMAIL = (By.ID, "correo")
    ADDRESS = (By.ID, "direccion")
    ADD_RESPONSIBLE_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[2]/input")
    ADD_RESPONSIBLE_ERROR_MSG = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[3]/strong")



class AddResponsibleOfStudentPage:
    def __init__(self, driver):
        self.driver = driver

    def is_header_displayed(self):
        return self.driver.wait_for_element_visible(AddResponsibleOfStudentLocators.PAGE_HEADER[0], AddResponsibleOfStudentLocators.PAGE_HEADER[1], 30)

    def is_add_responsible_error_displayed(self):
        return self.driver.wait_for_element_visible(AddResponsibleOfStudentLocators.ADD_RESPONSIBLE_ERROR_MSG[0], AddResponsibleOfStudentLocators.ADD_RESPONSIBLE_ERROR_MSG[1], 30)


    def enter_firstname(self, firstname):
        self.driver.send_keys(AddResponsibleOfStudentLocators.FIRST_NAME[0], AddResponsibleOfStudentLocators.FIRST_NAME[1], firstname)

    def enter_first_surname(self, first_surname):
        self.driver.send_keys(AddResponsibleOfStudentLocators.FIRST_SURNAME[0], AddResponsibleOfStudentLocators.FIRST_SURNAME[1], first_surname)

    def enter_second_surname(self, second_surname):
        self.driver.send_keys(AddResponsibleOfStudentLocators.SECOND_SURNAME[0], AddResponsibleOfStudentLocators.SECOND_SURNAME[1], second_surname)

    def enter_identification(self, identification):
        self.driver.send_keys(AddResponsibleOfStudentLocators.IDENTIFICATION[0], AddResponsibleOfStudentLocators.IDENTIFICATION[1], identification)

    def select_relationship(self, relationship):
        self.driver.set_combo_option(AddResponsibleOfStudentLocators.RELATIONSHIP[0], AddResponsibleOfStudentLocators.RELATIONSHIP[1], relationship)

    def enter_job(self, job):
        self.driver.send_keys(AddResponsibleOfStudentLocators.JOB[0], AddResponsibleOfStudentLocators.JOB[1], job)

    def enter_marital_status(self, marital_status):
        self.driver.send_keys(AddResponsibleOfStudentLocators.MARITAL_STATUS[0], AddResponsibleOfStudentLocators.MARITAL_STATUS[1], marital_status)

    def enter_nationality(self, nationality):
        self.driver.send_keys(AddResponsibleOfStudentLocators.NATIONALITY[0], AddResponsibleOfStudentLocators.NATIONALITY[1], nationality)

    def enter_phone_number(self, phone_number):
        self.driver.send_keys(AddResponsibleOfStudentLocators.PHONE_NUMBER[0], AddResponsibleOfStudentLocators.PHONE_NUMBER[1], phone_number)

    def enter_email(self, email):
        self.driver.send_keys(AddResponsibleOfStudentLocators.EMAIL[0], AddResponsibleOfStudentLocators.EMAIL[1], email)

    def enter_address(self, address):
        self.driver.send_keys(AddResponsibleOfStudentLocators.ADDRESS[0], AddResponsibleOfStudentLocators.ADDRESS[1], address)

    def click_submit_button(self):
        self.driver.click(*AddResponsibleOfStudentLocators.ADD_RESPONSIBLE_BUTTON)

    def is_add_responsible_of_student_error_displayed(self):
        return self.driver.wait_for_element_visible(AddResponsibleOfStudentLocators.ADD_RESPONSIBLE_ERROR_MSG[0], AddResponsibleOfStudentLocators.ADD_RESPONSIBLE_ERROR_MSG[1], 30)


