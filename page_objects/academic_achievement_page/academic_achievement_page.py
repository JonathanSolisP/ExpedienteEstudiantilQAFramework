from selenium.webdriver.common.by import By

__author__ = 'Proyecto'



class AcademicAchievementsLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    NAME_INPUT = (By.ID, "nombre")
    DESCRIPTION_INPUT = (By.ID, "descripcion")
    AWARD_INPUT = (By.ID, "premio")
    ERROR_MSG = (By.CLASS_NAME, "text-danger")
    ACADEMIC_ACHIEVEMENT_BUTTON = (By.ID, "btn_agregar_logro")


class AcademicAchievementPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(AcademicAchievementsLocators.TITLE, 30)

    def enter_name(self, name):
        self.driver.send_keys(AcademicAchievementsLocators.NAME_INPUT[0], AcademicAchievementsLocators.NAME_INPUT[1], name)

    def enter_description(self, description):
        self.driver.send_keys(AcademicAchievementsLocators.DESCRIPTION_INPUT[0], AcademicAchievementsLocators.DESCRIPTION_INPUT[1], description)

    def enter_award(self, award):
        self.driver.send_keys(AcademicAchievementsLocators.AWARD_INPUT[0], AcademicAchievementsLocators.AWARD_INPUT[1], award)

    def click_academic_achievement_button(self):
        self.driver.click(*AcademicAchievementsLocators.ACADEMIC_ACHIEVEMENT_BUTTON)

    def is_error_message_displayed(self):
        return self.driver.wait_for_element_visible(AcademicAchievementsLocators.ERROR_MSG[0], AcademicAchievementsLocators.ERROR_MSG[1], 30)
