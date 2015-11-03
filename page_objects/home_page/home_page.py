from selenium.webdriver.common.by import By


class HomeLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    STUDENT_TAB = (By.CLASS_NAME, "dropdown-toggle", 0)
    CREATE_STUDENT_TAB = (By.CSS_SELECTOR, "a.ng-binding")


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(HomeLocators.TITLE, 30)

    def click_student_tab(self):
        self.driver.click(HomeLocators.STUDENT_TAB[0], HomeLocators.STUDENT_TAB[1])

    def select_create_student_option(self):
        self.driver.click_from_elements(HomeLocators.CREATE_STUDENT_TAB[0], HomeLocators.CREATE_STUDENT_TAB[1], HomeLocators.CREATE_STUDENT_TAB[2])
