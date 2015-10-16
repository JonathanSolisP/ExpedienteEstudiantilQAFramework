from base.base_test import BaseTest

from page_objects.create_student_page.create_student_page import CreateStudentPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM

class CreateStudentTestSuite(BaseTest):

    def test_layout(self):
        create_student_page = CreateStudentPage(self.driver)
