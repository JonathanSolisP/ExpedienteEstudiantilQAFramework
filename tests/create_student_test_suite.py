from base.base_test import BaseTest

from page_objects.create_student_page.create_student_page import CreateStudentPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM
import time

class CreateStudentTestSuite(BaseTest):

    def test_layout(self):
        create_student_page = CreateStudentPage(self.driver)
        self.assertTrue(create_student_page.is_title_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
        create_student_page.enter_name("Hola mundo")
        create_student_page.select_gender("Femenino")
        time.sleep(5)
