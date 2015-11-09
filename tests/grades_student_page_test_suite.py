from base.base_test import BaseTest

from page_objects.grades_student_page.grades_student_page import GradesStudentPage
#from page_objects.grades_student_page.show_grades_student_page import ShowAcademicAchievementPage
from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage
from page_objects.view_student_page.view_student_page import ViewStudentPage
from configs.base_framework_configs import GlobalConfigs as GC
import time


class AddAcademicAchievementStudent(BaseTest):

    def go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()
        login_page = LoginPage(self.driver)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page.is_user_name_displayed()

    def test_set_grade_greater_than_100(self):
        self.go_to_page()
        my_url = "http://172.24.28.21:3000/#!/estudiantes/56392245bf6ad92638c8a0d6/notas_c_c"
        self.driver.get(my_url)
        assign_grades_student_page = GradesStudentPage(self.driver)
        assign_grades_student_page.click_ngCellText()
        #assign_grades_student_page.enter_grade("70")
        #assign_grades_student_page.enter_grade(101)
        #assign_grades_student_page.is_ngCellText_color()
        #self.assertEquals(assign_grades_student_page.is_ngCellText_color(), "ngCellText ng-binding")

        time.sleep(5)
