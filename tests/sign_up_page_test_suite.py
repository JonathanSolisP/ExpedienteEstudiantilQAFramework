from base.base_test import BaseTest
from page_objects.restore_password_page.restore_password_page import RestorePasswordPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM
from page_objects.sign_up_page.sign_up_page import SignUpPage

__author__ = 'Proyecto'


class RestorePasswordPageTest(BaseTest):

    def test_sign_up_successful(self):
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.enter_first_name("Josue")
        sign_up_page.enter_last_name("Morales")
        sign_up_page.enter_email("jocampos@gmail.com")
        sign_up_page.enter_username("jocampos")
        sign_up_page.enter_password("jocam1994")
        sign_up_page.click_sign_up_button()
        self.assertTrue(sign_up_page.is(), GM.MISSING_ERROR_MSG)

    def test_sign_up_empty_fields(self):
        restore_password_page = RestorePasswordPage(self.driver)
        restore_password_page.enter_username("test")
        restore_password_page.click_submit_button()
        self.assertTrue(restore_password_page.is_submit_username_error_displayed(), GM.MISSING_ERROR_MSG)

    def test_sign_up_existing_user(self):
        restore_password_page = RestorePasswordPage(self.driver)
        restore_password_page.enter_username("test")
        restore_password_page.click_submit_button()
        self.assertTrue(restore_password_page.is_submit_username_error_displayed(), GM.MISSING_ERROR_MSG)
