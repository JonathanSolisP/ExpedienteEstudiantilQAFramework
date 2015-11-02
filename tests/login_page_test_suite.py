import time

from base.base_test import BaseTest
from configs.base_framework_configs import GlobalConfigsMessages as GM
from configs.base_framework_configs import GlobalConfigs as GC
from page_objects.home_page.home_page import HomeLocators
from page_objects.login_page.login_page import LoginPage
from page_objects.home_page.home_page import HomePage

__author__ = 'Proyecto'


class LoginPageTestSuite(BaseTest):
    # def test_login_layout(self):
    #     login_page = LoginPage(self.driver)
    #     self.assertTrue(login_page.is_title_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
    #     login_page.enter_username("Hola mundo")
    #     time.sleep(5)


    def test_login_empty_fields(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_sign_in_button()
        self.assertTrue(login_page.is_sign_in_error_message_displayed(), GM.MISSING_CREDENTIALS_ERROR_MSG)
        time.sleep(5)

    def test_login_successful(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page = HomePage(self.driver)
        home_page.is_user_name_displayed()


    def test_login_invalid_user(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
        login_page.enter_username("NotAValidUser")
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        self.assertTrue(login_page.is_sign_in_error_message_displayed(),GM.UKNOWN_USER_OR_INVALID_PASSWORD_ERROR_MSG)


    def test_login_valid_user_invalid_password(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_displayed(), GM.ERROR_CREATE_STUDENT_PAGE)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password("N0T4V4L1DP4SSW0RD")
        login_page.click_sign_in_button()
        self.assertTrue(login_page.is_sign_in_error_message_displayed(),GM.UKNOWN_USER_OR_INVALID_PASSWORD_ERROR_MSG)
