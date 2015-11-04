from base.base_test import BaseTest

from page_objects.academic_achievement_page.academic_achievement_page import AcademicAchievementPage
from page_objects.create_student_page.create_student_page import CreateStudentPage
from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage
from page_objects.view_student_page.view_student_page import ViewStudentPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM
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
        home_page.click_student_tab()
        home_page.select_create_student_option()

    def test_add_academic_achievement_successful(self):
        self.go_to_page()
        create_academic_achievement_page = AcademicAchievementPage(self.driver)