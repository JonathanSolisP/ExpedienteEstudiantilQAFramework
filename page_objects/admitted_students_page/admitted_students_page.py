__author__ = 'Proyecto'
from selenium.webdriver.common.by import By
from base.base_test import BaseTest

class AdmitedStudentsLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    PAGE_HEADER = (By.XPATH, "/html/body/section/section/section/section/div[1]/h1")
    ADMITTED_STUDENTS_TABLE(By.XPATH, "/html/body/section/section/section/section/div[2]/div/div[2]")
    MIGRATE_STUDENT_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[3]/input")


class AddResponsibleOfStudentPage:
    def __init__(self, driver):
        self.driver = driver

    def is_header_displayed(self):
        return self.driver.wait_for_element_visible(AddResponsibleOfStudentLocators.PAGE_HEADER[0], AddResponsibleOfStudentLocators.PAGE_HEADER[1], 30)

    def enter_value(self, value):
        self.driver.send_keys(AddResponsibleOfStudentLocators.FIRST_NAME[0], AddResponsibleOfStudentLocators.FIRST_NAME[1], firstname)

