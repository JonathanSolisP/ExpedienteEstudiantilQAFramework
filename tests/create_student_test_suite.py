from base.base_test import BaseTest

from page_objects.create_student_page.create_student_page import CreateStudentPage
from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage
from page_objects.view_student_page.view_student_page import ViewStudentPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM
import time


class CreateStudentTestSuite(BaseTest):

    def go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()
        login_page = LoginPage(self.driver)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page.is_user_name_displayed()
        home_page.click_student_tab()
        home_page.select_create_student_option()

    def test_create_student_layout(self):
        self.go_to_page()
        create_student_page = CreateStudentPage(self.driver)
        self.assertTrue(create_student_page.is_header_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)

    def test_create_student_empty_fields(self):
        self.go_to_page()
        create_student_page = CreateStudentPage(self.driver)
        create_student_page.click_create_student()
        self.assertTrue(create_student_page.is_header_displayed(), GM.ERROR_CREATE_STUDENT_PAGE_INVALID_DATA)
        time.sleep(2)

    def test_create_student_successful(self):
        self.go_to_page()
        create_student_page = CreateStudentPage(self.driver)
        create_student_page.enter_name(GC.NAME)
        create_student_page.enter_first_last_name(GC.FIRST_LAST_NAME)
        create_student_page.enter_second_last_name(GC.SECOND_LAST_NAME)
        create_student_page.enter_birthday(GC.BIRTHDAY)
        create_student_page.enter_id_number(GC.ID_NUMBER)
        create_student_page.select_gender(GC.GENDER)
        create_student_page.enter_phone_number(GC.PHONE_NUMBER)
        create_student_page.enter_cell_phone_number(GC.CELL_PHONE_NUMBER)
        create_student_page.enter_email(GC.EMAIL)
        create_student_page.select_province(GC.PROVINCE)
        create_student_page.select_canton(GC.CANTON)
        create_student_page.select_district(GC.DISTRICT)
        create_student_page.enter_neighborhood(GC.NEIGHBORHOOD)
        create_student_page.enter_address(GC.ADDRESS)
        create_student_page.select_high_school(GC.HIGH_SCHOOL)
        create_student_page.enter_income_year(GC.INCOME_YEAR)
        create_student_page.set_graduated()
        create_student_page.select_meaningful_adequacy(GC.MEANINGFUL_ADEQUACY)
        create_student_page.select_not_meaningful_adequacy(GC.NOT_MEANINGFUL_ADEQUACY)
        create_student_page.click_create_student()
        view_student_page = ViewStudentPage(self.driver)
        self.assertTrue(view_student_page.is_add_responsible_button_displayed(), GM.ERROR_CREATE_STUDENT_PAGE_SUBMIT)
