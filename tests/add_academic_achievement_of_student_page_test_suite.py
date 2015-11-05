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
        ###home_page.click_student_tab()
        ###home_page.select_create_student_option()

    def test_add_academic_achievement_successful(self):
        self.go_to_page()
        my_url = "http://172.24.28.21:3000/#!/logros-academicos/create/56392245bf6ad92638c8a0d6/207320402"
        self.driver.get(my_url)
        create_academic_achievement_page = AcademicAchievementPage(self.driver)
        create_academic_achievement_page.enter_name("Premio")
        create_academic_achievement_page.enter_description("Juegos")
        create_academic_achievement_page.enter_award("Medalla")
        create_academic_achievement_page.click_academic_achievement_button()
        viewStudentPage = ViewStudentPage(self.driver)
        viewStudentPage.is_add_responsible_button_displayed()
        time.sleep(5)

    def test_add_academic_achievement_empty_fields(self):
        self.go_to_page()
        my_url = "http://172.24.28.21:3000/#!/logros-academicos/create/56392245bf6ad92638c8a0d6/207320402"
        self.driver.get(my_url)
        create_academic_achievement_page = AcademicAchievementPage(self.driver)
        create_academic_achievement_page.enter_name("Premio")
        create_academic_achievement_page.enter_description("Juegos")
        create_academic_achievement_page.click_academic_achievement_button()
        create_academic_achievement_page.is_error_message_displayed()
        time.sleep(5)
