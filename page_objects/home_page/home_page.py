from selenium.webdriver.common.by import By


class HomeLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    SLOGAN = "Ser mejores, para servir mejor a Costa Rica"
    USERNAME = (By.XPATH, "/html/body/header/div/nav/ul[3]/li/a/span")

    STUDENT_TAB = (By.CLASS_NAME, "dropdown-toggle", 0)
    FUNCTIONARY_TAB = (By.CLASS_NAME, "dropdown-toggle", 1)

    CREATE_STUDENT_TAB = (By.CSS_SELECTOR, "a.ng-binding", 0)
    DISPLAY_STUDENT_IN_ADMISSION_TAB = (By.CSS_SELECTOR, "a.ng-binding", 1)
    DISPLAY_ADMITTED_STUDENT_TAB = (By.CSS_SELECTOR, "a.ng-binding", 2)
    CONSULT_STUDENT_TAB = (By.CSS_SELECTOR, "a.ng-binding", 3)
    REPORTS_STUDENT_TAB = (By.CSS_SELECTOR, "a.ng-binding", 4)

    FUNCTIONARY_LIST_TAB = (By.CSS_SELECTOR, "a.ng-binding", 1)
    NEW_FUNCTIONARY_TAB = (By.CSS_SELECTOR, "a.ng-binding", 2)

    SIGN_UP_TAB = (By.XPATH, "//li[@class='ng-scope']//a[contains(@href, '#!/sign')]", 0)
    SIGN_IN_TAB = (By.XPATH, "//li[@class='ng-scope']//a[contains(@href, '#!/sign')]", 1)


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(HomeLocators.TITLE, 30)

    def is_user_name_displayed(self,):
        return self.driver.wait_for_element_visible(HomeLocators.USERNAME[0], HomeLocators.USERNAME[1], 30)

    def click_student_tab(self):
        self.driver.click_from_elements(HomeLocators.STUDENT_TAB[0], HomeLocators.STUDENT_TAB[1], HomeLocators.STUDENT_TAB[2])

    def click_functionary_tab(self):
        self.driver.click_from_elements(HomeLocators.FUNCTIONARY_TAB[0], HomeLocators.FUNCTIONARY_TAB[1], HomeLocators.FUNCTIONARY_TAB[2])

    def select_create_student_option(self):
        self.driver.click_from_elements(HomeLocators.CREATE_STUDENT_TAB[0], HomeLocators.CREATE_STUDENT_TAB[1], HomeLocators.CREATE_STUDENT_TAB[2])

    def select_new_functionary_option(self):
        self.driver.click_from_elements(HomeLocators.NEW_FUNCTIONARY_TAB[0], HomeLocators.NEW_FUNCTIONARY_TAB[1], HomeLocators.NEW_FUNCTIONARY_TAB[2])

    def select_functionary_list_option(self):
        self.driver.click_from_elements(HomeLocators.FUNCTIONARY_LIST_TAB[0], HomeLocators.FUNCTIONARY_LIST_TAB[1], HomeLocators.FUNCTIONARY_LIST_TAB[2])

    def select_display_student_in_admission_option(self):
        self.driver.click_from_elements(HomeLocators.DISPLAY_STUDENT_IN_ADMISSION_TAB[0], HomeLocators.DISPLAY_STUDENT_IN_ADMISSION_TAB[1], HomeLocators.DISPLAY_STUDENT_IN_ADMISSION_TAB[2])

    def select_display_admitted_student_option(self):
        self.driver.click_from_elements(HomeLocators.DISPLAY_ADMITTED_STUDENT_TAB[0], HomeLocators.DISPLAY_ADMITTED_STUDENT_TAB[1], HomeLocators.DISPLAY_ADMITTED_STUDENT_TAB[2])

    def select_consult_student_option(self):
        self.driver.click_from_elements(HomeLocators.CONSULT_STUDENT_TAB[0], HomeLocators.CONSULT_STUDENT_TAB[1], HomeLocators.CONSULT_STUDENT_TAB[2])

    def select_reports_student_tab(self):
        self.driver.click_from_elements(HomeLocators.REPORTS_STUDENT_TAB[0], HomeLocators.REPORTS_STUDENT_TAB[1], HomeLocators.REPORTS_STUDENT_TAB[2])

    def click_sign_up(self):
        self.driver.click_from_elements(HomeLocators.SIGN_UP_TAB[0], HomeLocators.SIGN_UP_TAB[1], HomeLocators.SIGN_UP_TAB[2])

    def click_sign_in(self):
        self.driver.click_from_elements(HomeLocators.SIGN_IN_TAB[0], HomeLocators.SIGN_IN_TAB[1], HomeLocators.SIGN_IN_TAB[2])
