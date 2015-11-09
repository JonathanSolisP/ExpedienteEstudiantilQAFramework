__author__ = 'Proyecto'


class SearchFunctionaryResumeLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    QUERY_INPUT = (By.XPATH, "/html/body/section/section/section/section/div[2]/div/input")
    FUNCTIONARY_RESUME_REF = (By.XPATH, "/html/body/section/section/section/section/div[4]/div/a")
    DELETE_FUNCTIONARY_BUTTON = (By.XPATH, "/html/body/section/section/section/section/div[4]/div/a/div/div/small/span[2]/button")

class SearchFunctionaryResumePage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(RestorePasswordLocators.TITLE, 30)

    def enter_query(self, query):
        self.driver.send_keys(SearchFunctionaryResumeLocators.QUERY_INPUT[0], SearchFunctionaryResumeLocators.QUERY_INPUT[1], query)

    def click_submit_button(self):
        self.driver.click(*SearchFunctionaryResumeLocators)

