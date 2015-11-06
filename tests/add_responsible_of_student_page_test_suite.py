from base.base_test import BaseTest
from page_objects.add_responsible_of_student_page.add_responsible_of_student_page import AddResponsibleOfStudentPage
from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage
from page_objects.view_student_page.view_student_page import ViewStudentPage
from configs.base_framework_configs import GlobalConfigsMessages as GM
from configs.base_framework_configs import GlobalConfigs as GC
import time
__author__ = 'Proyecto'


class AddResponsibleOfStudentTestSuite(BaseTest):

    def go_to_responsible_of_student_page(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()
        login_page = LoginPage(self.driver)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page.is_user_name_displayed()
        home_page.click_student_tab()
        home_page.select_display_admitted_student_option()
        self.driver.get("http://172.24.28.21:3000/#!/estudiantes/55fad571f2e6997805459141")
        view_student_page = ViewStudentPage(self.driver)
        view_student_page.is_add_responsible_button_displayed()
        view_student_page.click_add_responsible()

    def test_add_responsible_student_layout(self):
        self.go_to_responsible_of_student_page()
        add_responsible_of_student_page = AddResponsibleOfStudentPage(self.driver)
        self.assertTrue(add_responsible_of_student_page.is_header_displayed(), GM.MISSING_ERROR_MSG)

    def test_add_responsible_student_successful(self):
        self.go_to_responsible_of_student_page()
        add_responsible_of_student_page = AddResponsibleOfStudentPage(self.driver)
        add_responsible_of_student_page.enter_firstname("Maria")
        add_responsible_of_student_page.enter_first_surname("Perez")
        add_responsible_of_student_page.enter_second_surname("Mora")
        add_responsible_of_student_page.enter_identification("201232974")
        add_responsible_of_student_page.select_relationship("Madre")
        add_responsible_of_student_page.enter_job("Ingeniera Quimico")
        add_responsible_of_student_page.enter_phone_number("12345678")
        add_responsible_of_student_page.enter_marital_status("Casada")
        add_responsible_of_student_page.enter_nationality("Costarricense")
        add_responsible_of_student_page.enter_email("jorgeperez@gmail.com")
        add_responsible_of_student_page.enter_address("Ciudad Quesada")
        add_responsible_of_student_page.click_submit_button()
        view_student_page = ViewStudentPage(self.driver)
        self.assertTrue(view_student_page.is_add_responsible_button_displayed(), GM.ERROR_ADD_RESPONSIBLE_SUBMIT)

    def test_add_responsible_student_has_two_responsibles(self):
        self.go_to_responsible_of_student_page()
        add_responsible_of_student_page = AddResponsibleOfStudentPage(self.driver)
        add_responsible_of_student_page.enter_firstname("Maria")
        add_responsible_of_student_page.enter_first_surname("Perez")
        add_responsible_of_student_page.enter_second_surname("Mora")
        add_responsible_of_student_page.enter_identification("201232974")
        add_responsible_of_student_page.select_relationship("Madre")
        add_responsible_of_student_page.enter_job("Ingeniera Quimico")
        add_responsible_of_student_page.enter_phone_number("12345678")
        add_responsible_of_student_page.enter_marital_status("Casada")
        add_responsible_of_student_page.enter_nationality("Costarricense")
        add_responsible_of_student_page.enter_email("jorgeperez@gmail.com")
        add_responsible_of_student_page.enter_address("Ciudad Quesada")
        add_responsible_of_student_page.click_submit_button()
        self.assertTrue(add_responsible_of_student_page.is_add_responsible_error_displayed(), GM.ERROR_ADD_RESPONSIBLE_SUBMIT)

    def test_add_responsible_of_student_empty_fields(self):
        self.go_to_responsible_of_student_page()
        add_responsible_of_student_page = AddResponsibleOfStudentPage(self.driver)
        add_responsible_of_student_page.click_submit_button()
        self.assertTrue(add_responsible_of_student_page.is_header_displayed(), GM.MISSING_ERROR_MSG)


