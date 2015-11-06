from page_objects.home_page.home_page import HomePage
from page_objects.login_page.login_page import LoginPage

__author__ = 'Proyecto'

from base.base_test import BaseTest
from page_objects.add_new_functionary_page.add_new_functionary_page import AddNewFunctionaryPage
from configs.base_framework_configs import GlobalConfigsMessages as GM
from configs.base_framework_configs import GlobalConfigs as GC

class AddNewFunctionaryPageTest(BaseTest):
    def go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()
        login_page = LoginPage(self.driver)
        login_page.enter_username(GC.USERNAME)
        login_page.enter_password(GC.PASSWORD)
        login_page.click_sign_in_button()
        home_page.is_user_name_displayed()

    def test_add_new_functionary_successful(self):
        add_new_functionary_page = AddNewFunctionaryPage(self.driver)
        add_new_functionary_page.enter_first_name("Jorge")
        add_new_functionary_page.enter_first_surname("Gomez")
        add_new_functionary_page.enter_second_surname("Gomez")
        add_new_functionary_page.enter_identification("304820160")
        add_new_functionary_page.enter_birthdate("01/04/1994")
        add_new_functionary_page.select_marital_status("Soltero")
        add_new_functionary_page.enter_address("Ciudad Quesada")
        add_new_functionary_page.enter_phone_number("12345678")
        add_new_functionary_page.enter_cellphone_number("12345678")
        add_new_functionary_page.enter_email("jorgeperez@gmail.com")
        add_new_functionary_page.select_role("Academico")
        add_new_functionary_page.enter_hire_date("06/06/2006")
        add_new_functionary_page.select_status("Activo")
        add_new_functionary_page.click_save_button()
        self.assertTrue(add_new_functionary_page.is_save_new_functionary_error_message_display(),GM.MISSING_ERROR_MSG)


    def add_new_functionary_existant_functionary(self):
        add_new_functionary_page = AddNewFunctionaryPage(self.driver)
        add_new_functionary_page.enter_first_name("Jorge")
        add_new_functionary_page.enter_first_surname("Gomez")
        add_new_functionary_page.enter_second_surname("Gomez")
        add_new_functionary_page.enter_identification("304820160")
        add_new_functionary_page.enter_birthdate("01/04/1994")
        add_new_functionary_page.select_marital_status("Soltero")
        add_new_functionary_page.enter_address("Ciudad Quesada")
        add_new_functionary_page.enter_phone_number("12345678")
        add_new_functionary_page.enter_cellphone_number("12345678")
        add_new_functionary_page.enter_email("jorgeperez@gmail.com")
        add_new_functionary_page.select_role("Academico")
        add_new_functionary_page.enter_hire_date("06/06/2006")
        add_new_functionary_page.select_status("Activo")
        add_new_functionary_page.click_save_button()
        self.assertTrue(add_new_functionary_page.is_save_new_functionary_error_message_display(),GM.MISSING_ERROR_MSG)

    def test_add_new_functionary_empty_fields(self):
        add_new_functionary_page = AddNewFunctionaryPage(self.driver)
        self.assertTrue(add_new_functionary_page.is_save_new_functionary_error_message_display(),GM.MISSING_ERROR_MSG)

