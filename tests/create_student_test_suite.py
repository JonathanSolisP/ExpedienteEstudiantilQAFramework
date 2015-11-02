from base.base_test import BaseTest

from page_objects.create_student_page.create_student_page import CreateStudentPage
from page_objects.home_page.home_page import HomePage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM
import time


class CreateStudentTestSuite(BaseTest):

    def go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.click_student_tab()
        home_page.select_create_student_option()
        self.assertTrue(home_page.is_title_displayed(), GM.ERROR_HOME_PAGE)

    def test_create_student_layout(self):
        self.go_to_page()
        create_student_page = CreateStudentPage(self.driver)
        self.assertTrue(create_student_page.is_header_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
