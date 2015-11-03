from base.base_test import BaseTest
from page_objects.add_responsible_of_student_page.add_responsible_of_student_page import AddResponsibleOfStudentPage

__author__ = 'Proyecto'

from configs.base_framework_configs import GlobalConfigsMessages as GM

class AddResponsibleOfStudentTestSuite(BaseTest):



    def test_add_responsible_student_successful(self):
        add_responsible_of_student_page = AddResponsibleOfStudentPage(self.driver)
        add_responsible_of_student_page.enter_firstname("Jorge")
        add_responsible_of_student_page.enter_first_surname("Perez")
        add_responsible_of_student_page.enter_second_surname("Perez")
        add_responsible_of_student_page.enter_identification("201232974")
        add_responsible_of_student_page.enter_job("Ingeniero Quimico")
        add_responsible_of_student_page.enter_phone_number("12345678")
        add_responsible_of_student_page.enter_marital_status("ThisIsNotACombo")
        add_responsible_of_student_page.enter_phone_number("12345678")
        add_responsible_of_student_page.enter_email("jorgeperez@gmail.com")
        add_responsible_of_student_page.enter_address("Ciudad Quesada")
        add_responsible_of_student_page.click_submit_button()
        self.assertTrue(add_responsible_of_student_page.is_header_displayed(),GM.HEADER_NOT_DISPLAYED)

    def test_add_responsible_of_student_empty_fields(self):
        add_responsible_of_student_page = AddResponsibleOfStudentPage(self.driver)
        add_responsible_of_student_page.click_submit_button()
        self.assertTrue(add_responsible_of_student_page.is_header_displayed(),GM.MISSING_ERROR_MSG)


