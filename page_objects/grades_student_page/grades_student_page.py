from selenium.webdriver.common.by import By

__author__ = 'Proyecto'


class GradesStudentLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    SPANISH_TENTH_NCELLTEXT = (By.XPATH, "/html/body/section/section/section/section/form/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div")
    ERROR_MSG = (By.CLASS_NAME, "text-danger")
    ASSIGN_GRADES_STUDENT_BUTTON = (By.ID, "Asignar_notas")


class GradesStudentPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(GradesStudentLocators.TITLE, 30)

    def enter_grade(self, grade):
        self.driver.send_keys(GradesStudentLocators.SPANISH_TENTH_NCELLTEXT[0], GradesStudentLocators.SPANISH_TENTH_NCELLTEXT[1], grade)

    def is_ngCellText_color(self):
        attribute = self.driver.get_attribute(GradesStudentLocators.SPANISH_TENTH_NCELLTEXT[0],
                                  GradesStudentLocators.SPANISH_TENTH_NCELLTEXT[1],
                                  'class')
        return attribute

    def click_assign_grades_student_button(self):
        self.driver.click(*GradesStudentLocators.ASSIGN_GRADES_STUDENT_BUTTON)

    def is_error_message_displayed(self):
        return self.driver.wait_for_element_visible(GradesStudentLocators.ERROR_MSG[0], GradesStudentLocators.ERROR_MSG[1], 30)
