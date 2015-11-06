__author__ = 'Proyecto'

from selenium.webdriver.common.by import By


class QueryStudentsLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    HEADER = (By.XPATH, "//div[@class='page-header']/h1")
    QUERY_TYPE = (By.ID, "consulta")
    QUERY_TEXT = (By. XPATH, "//div[@class='controls']/input")
    QUERY_GENDER = (By.ID, "consulta_sexo")
    QUERY_GRADE = (By.ID, "consulta_grado")
    QUERY_STATE = (By.ID, "consulta_estado")


class QueryStudentsPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(QueryStudentsLocators.TITLE, 30)

    def is_header_displayed(self):
        return self.driver.wait_for_element_visible(QueryStudentsLocators.HEADER[0], QueryStudentsLocators.HEADER[1], 30) is not None

    def select_query_type(self, query_type):
        self.driver.set_combo_option(QueryStudentsLocators.QUERY_TYPE[0], QueryStudentsLocators.QUERY_TYPE[1], query_type)

    def enter_query_text(self, query_text):
        self.driver.send_keys(QueryStudentsLocators.QUERY_TEXT[0], QueryStudentsLocators.QUERY_TEXT[1], query_text)

    def select_query_gender(self, query_gender):
        self.driver.set_combo_option(QueryStudentsLocators.QUERY_TYPE[0], QueryStudentsLocators.QUERY_GENDER[1], query_gender)

    def select_query_grade(self, query_grade):
        self.driver.set_combo_option(QueryStudentsLocators.QUERY_TYPE[0], QueryStudentsLocators.QUERY_GRADE[1], query_grade)

    def select_query_state(self, query_state):
        self.driver.set_combo_option(QueryStudentsLocators.QUERY_TYPE[0], QueryStudentsLocators.QUERY_STATE[1], query_state)




