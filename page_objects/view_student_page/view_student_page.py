__author__ = 'Proyecto'
from selenium.webdriver.common.by import By


class ViewStudentLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    HEADER = (By.XPATH, "//div[@class='page-header']/h1")
    ADD_RESPONSIBLE_BUTTON = (By.XPATH, "//input[@value='Asignar encargados']")


class ViewStudentPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(ViewStudentLocators.TITLE, 30)

    def is_header_displayed(self):
        return self.driver.wait_for_element_present(ViewStudentLocators.HEADER[0], ViewStudentLocators.HEADER[1], 30) is not None

    def is_add_responsible_button_displayed(self):
        return self.driver.wait_for_element_visible(ViewStudentLocators.ADD_RESPONSIBLE_BUTTON[0], ViewStudentLocators.ADD_RESPONSIBLE_BUTTON[1], 30) is not None

    def click_add_responsible(self):
        self.driver.click(ViewStudentLocators.ADD_RESPONSIBLE_BUTTON[0], ViewStudentLocators.ADD_RESPONSIBLE_BUTTON[1])
