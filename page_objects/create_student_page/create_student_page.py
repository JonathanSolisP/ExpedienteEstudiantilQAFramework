class CreateStudentLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"

class CreateStudentPage():
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(CreateStudentLocators.TITLE, 30)

