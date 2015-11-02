from selenium.webdriver.common.by import By


class CreateStudentLocators:

    def __init__(self):
        pass

    TITLE = "Expediente Estudiantil - Development Environment"
    HEADER = (By.XPATH, "//div[@class='page-header']/h1")
    NAME_INPUT = (By.ID, "name")
    FIRST_LAST_NAME_INPUT = (By.ID, "primer_apellido")
    SECOND_LAST_NAME_INPUT = (By.ID, "segundo_apellido")
    BIRTHDAY_INPUT = (By.ID, "fecha_de_nacimiento")
    ID_NUMBER_INPUT = (By.ID, "nacionalidad")
    GENDER_COMBO = (By.ID, "sexo")
    PHONE_NUMBER_INPUT = (By.ID, "telefono_casa")
    CELL_PHONE_NUMBER_INPUT = (By.ID, "celular")
    EMAIL_INPUT = (By.ID, "correo")
    PROVINCE_COMBO = (By.ID, "provincia")
    CANTON_COMBO = (By.ID, "canton")
    DISTRICT_COMBO = (By.ID, "distrito")
    NEIGHBORHOOD_INPUT = (By.ID, "barrio")
    ADDRESS_INPUT = (By.ID, "direccion_exacta")
    INCOME_YEAR_INPUT = (By.ID, "anno_ingreso")
    GRADUATED_CHECKBOX = (By.NAME, "graduado")
    MEANINGFUL_ADEQUACY_COMBO = (By.ID, "adecuacion_significativa")
    NOT_MEANINGFUL_ADEQUACY_COMBO = (By.ID, "adecuacion_nsignificativa")
    CREATE_STUDENT_BUTTON = (By.CLASS_NAME, "btn-primary")


class CreateStudentPage:
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        return self.driver.wait_for_title_contains(CreateStudentLocators.TITLE, 30)

    def is_header_displayed(self):
        return self.driver.wait_for_element_present(CreateStudentLocators.HEADER[0], CreateStudentLocators.HEADER[1], 30) is not None

    def enter_name(self, name):
        self.driver.send_keys(CreateStudentLocators.NAME_INPUT[0], CreateStudentLocators.NAME_INPUT[1], name)

    def enter_first_last_name(self, first_last_name):
        self.driver.send_keys(CreateStudentLocators.FIRST_LAST_NAME_INPUT[0], CreateStudentLocators.FIRST_LAST_NAME_INPUT[1], first_last_name)

    def enter_second_last_name(self, second_last_name):
        self.driver.send_keys(CreateStudentLocators.SECOND_LAST_NAME_INPUT[0], CreateStudentLocators.SECOND_LAST_NAME_INPUT[1], second_last_name)

    def enter_birthday(self, birthday):
        self.driver.send_keys(CreateStudentLocators.BIRTHDAY_INPUT[0], CreateStudentLocators.BIRTHDAY_INPUT[1], birthday)

    def enter_id_number(self, id_number):
        self.driver.send_keys(CreateStudentLocators.ID_NUMBER_INPUT[0], CreateStudentLocators.ID_NUMBER_INPUT[1], id_number)

    def select_gender(self, gender):
        self.driver.set_combo_option(CreateStudentLocators.GENDER_COMBO[0], CreateStudentLocators.GENDER_COMBO[1], gender)

    def enter_phone_number(self, phone_number):
        self.driver.send_keys(CreateStudentLocators.PHONE_NUMBER_INPUT[0], CreateStudentLocators.PHONE_NUMBER_INPUT[1], phone_number)

    def enter_cell_phone_number(self, cell_phone_number):
        self.driver.send_keys(CreateStudentLocators.CELL_PHONE_NUMBER_INPUT[0], CreateStudentLocators.CELL_PHONE_NUMBER_INPUT[1], cell_phone_number)

    def enter_email(self, email):
        self.driver.send_keys(CreateStudentLocators.EMAIL_INPUT[0], CreateStudentLocators.EMAIL_INPUT[1], email)

    def select_province(self, province):
        self.driver.set_combo_option(CreateStudentLocators.PROVINCE_COMBO[0], CreateStudentLocators.PROVINCE_COMBO[1], province)

    def select_canton(self, canton):
        self.driver.set_combo_option(CreateStudentLocators.CANTON_COMBO[0], CreateStudentLocators.CANTON_COMBO[1], canton)

    def select_district(self, district):
        self.driver.set_combo_option(CreateStudentLocators.DISTRICT_COMBO[0], CreateStudentLocators.DISTRICT_COMBO[1], district)

    def enter_neighborhood(self, neighborhood):
        self.driver.send_keys(CreateStudentLocators.NEIGHBORHOOD_INPUT[0], CreateStudentLocators.NEIGHBORHOOD_INPUT[1], neighborhood)

    def enter_address(self, address):
        self.driver.send_keys(CreateStudentLocators.ADDRESS_INPUT[0], CreateStudentLocators.ADDRESS_INPUT[1], address)

    def enter_income_year(self, income_year):
        self.driver.send_keys(CreateStudentLocators.INCOME_YEAR_INPUT[0], CreateStudentLocators.INCOME_YEAR_INPUT[1], income_year)

    def set_graduated(self):
        self.driver.click(CreateStudentLocators.GRADUATED_CHECKBOX[0], CreateStudentLocators.GRADUATED_CHECKBOX[1])

    def select_meaningful_adequacy(self, adequacy):
        self.driver.set_combo_option(CreateStudentLocators.MEANINGFUL_ADEQUACY_COMBO[0], CreateStudentLocators.MEANINGFUL_ADEQUACY_COMBO[1], adequacy)

    def select_not_meaningful_adequacy(self, adequacy):
        self.driver.set_combo_option(CreateStudentLocators.NOT_MEANINGFUL_ADEQUACY_COMBO[0], CreateStudentLocators.NOT_MEANINGFUL_ADEQUACY_COMBO[1], adequacy)

    def click_create_student(self):
        self.driver.click(CreateStudentLocators.CREATE_STUDENT_BUTTON[0], CreateStudentLocators.CREATE_STUDENT_BUTTON[1])






