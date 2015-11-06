from base.base_test import BaseTest

from page_objects.academic_achievement_page.academic_achievement_page import AcademicAchievementPage
from page_objects.academic_achievement_page.show_academic_achievement_page import ShowAcademicAchievementPage
from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage
from page_objects.view_student_page.view_student_page import ViewStudentPage
from configs.base_framework_configs import GlobalConfigs as GC


class AddAcademicAchievementStudent(BaseTest):

    def go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()
        login_page = LoginPage(self.driver)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page.is_user_name_displayed()

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

    def test_add_academic_achievement_empty_fields(self):
        self.go_to_page()
        my_url = "http://172.24.28.21:3000/#!/logros-academicos/create/56392245bf6ad92638c8a0d6/207320402"
        self.driver.get(my_url)
        create_academic_achievement_page = AcademicAchievementPage(self.driver)
        create_academic_achievement_page.enter_name("Premio")
        create_academic_achievement_page.enter_description("Juegos")
        create_academic_achievement_page.click_academic_achievement_button()
        create_academic_achievement_page.is_error_message_displayed()

    def test_delete_academic_achievement_successfull(self):
        self.go_to_page()
        my_url = "http://172.24.28.21:3000/#!/logros-academicos/56392245bf6ad92638c8a0d6//563b7feebf6ad92638c8a1cf"
        self.driver.get(my_url)
        delete_academic_achievement_page = ShowAcademicAchievementPage(self.driver)
        delete_academic_achievement_page.click_delete_academic_achievement_button()
        delete_academic_achievement_page.is_header_show_displayed()


