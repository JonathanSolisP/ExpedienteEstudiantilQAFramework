__author__ = 'Proyecto'

from base.base_test import BaseTest

from page_objects.home_page.home_page import HomePage
from configs.base_framework_configs import GlobalConfigsMessages as GM


class HomePageTestSuite(BaseTest):

    def test_home_page_layout(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_title_displayed(), GM.ERROR_HOME_PAGE)

