from base.base_test import BaseTest
from page_objects.restore_password_page.restore_password_page import RestorePasswordPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM

__author__ = 'Proyecto'

class RestorePasswordPageTest(BaseTest):


    def test_restore_password_empty_username(self):
        restore_password_page = RestorePasswordPage(self.driver)
        restore_password_page.enter_username("")
        restore_password_page.click_submit_button()
        self.assertTrue(restore_password_page.is_submit_username_error_displayed(), GM.USERNAME_FIELD_BLANK_ERROR_MSG)

    def retore_password_invalid_username(self):
        restore_password_page = RestorePasswordPage(self.driver)
        restore_password_page.enter_username("test")
        restore_password_page.click_submit_button()
        self.assertTrue(restore_password_page.is_submit_username_error_displayed(), GM.NO_ACCOUNT_FOUND_WITH_THAT_USERNAME_ERROR_MSG)

##!
    def restore_password_valid_username(self):
        restore_password_page = RestorePasswordPage(self.driver)
        restore_password_page.enter_username(GC.USERNAME)
        restore_password_page.click_submit_button()

