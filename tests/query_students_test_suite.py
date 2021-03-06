__author__ = 'Proyecto'
from base.base_test import BaseTest

from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage
from page_objects.query_student_page.query_student_page import QueryStudentsPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM


class QueryStudentsTestSuite(BaseTest):

    def go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()
        login_page = LoginPage(self.driver)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page.is_user_name_displayed()
        home_page.click_student_tab()
        home_page.select_consult_student_option()

    def test_query_students_layout(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        self.assertTrue(query_students_page.is_header_displayed(), GM.ERROR_QUERY_STUDENTS_PAGE)

    def test_query_by_name_specific_gender_specific_grade_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_specific_gender_specific_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_specific_gender_specific_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_specific_gender_both_grades_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_specific_gender_both_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_specific_gender_both_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_both_genders_specific_grade_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_BOTH_GENDERS)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_both_genders_specific_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_BOTH_GENDERS)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_both_genders_specific_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_BOTH_GENDERS)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_both_genders_both_grades_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_BOTH_GENDERS)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_both_genders_both_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_BOTH_GENDERS)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_name_both_genders_both_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_NAME)
        query_students_page.select_query_gender(GC.QUERY_BOTH_GENDERS)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_specific_gender_specific_grade_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_specific_gender_specific_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_specific_gender_specific_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_specific_gender_both_grades_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_specific_gender_both_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_specific_gender_both_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_both_genders_specific_grade_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_both_genders_specific_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_both_genders_specific_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_both_genders_both_grades_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH )
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_both_genders_both_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_identification_both_genders_both_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_IDENTIFICATION)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_specific_gender_specific_grade_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_specific_gender_specific_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_specific_gender_specific_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_specific_gender_both_grades_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH )
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_specific_gender_both_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_specific_gender_both_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_both_genders_specific_grade_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_both_genders_specific_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_both_genders_specific_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_both_genders_both_grades_all(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_ALL)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_both_genders_both_grade_graduated(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_GRADUATED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)

    def test_query_by_high_school_both_genders_both_grade_transferred(self):
        self.go_to_page()
        query_students_page = QueryStudentsPage(self.driver)
        query_students_page.select_query_type(GC.QUERY_HIGH_SCHOOL)
        query_students_page.select_query_gender(GC.QUERY_MALE)
        query_students_page.select_query_grade(GC.QUERY_TENTH_AND_ELEVENTH)
        query_students_page.select_query_state(GC.QUERY_TRANSFERRED)
        self.assertTrue(query_students_page.is_content_correct(), GM.ERROR_QUERY_STUDENTS_FAILED)





