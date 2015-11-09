from selenium.webdriver.common.by import By

__author__ = 'Proyecto'


class ShowAcademicAchievementsLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    DELETE_ACADEMIC_ACHIEVEMENT_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[2]/a[2]")
    HEADER_ACADEMIC_ACHIEVEMENT_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[1]/h1")
    UPDATE_ACADEMIC_ACHIEVEMENT_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[2]/form/fieldset/div[2]/input")
    NAME_ACADEMIC_AWARD = (By.XPATH, "/html/body/section/section/section/section/div[1]/h1")





class ShowAcademicAchievementPage:
    def __init__(self, driver):
        self.driver = driver

    def click_delete_academic_achievement_button(self):
        self.driver.click(*ShowAcademicAchievementsLocators.DELETE_ACADEMIC_ACHIEVEMENT_BUTTON)

    def click_update_academic_achievement_button(self):
        self.driver.click(*ShowAcademicAchievementsLocators.UPDATE_ACADEMIC_ACHIEVEMENT_BUTTON)

    def is_header_show_displayed(self):
        return self.driver.wait_for_element_visible(ShowAcademicAchievementsLocators.HEADER_ACADEMIC_ACHIEVEMENT_BUTTON[0],
                                                    ShowAcademicAchievementsLocators.HEADER_ACADEMIC_ACHIEVEMENT_BUTTON[1], 30)

    def is_name_academic_award_displayed(self):
        return self.driver.wait_for_element_visible(ShowAcademicAchievementsLocators.NAME_ACADEMIC_AWARD[0],
                                                    ShowAcademicAchievementsLocators.NAME_ACADEMIC_AWARD[1], 30)


