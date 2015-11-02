from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from configs.base_framework_configs import GlobalConfigsMessages as GM

from selenium import webdriver
from driver.browser_type import BrowserType as BrowserType


class ActionBot:
    def __init__(self, browser_type):
        if browser_type != "":
            print GM.SELECTED_BROWSER + browser_type
            if browser_type == BrowserType.FIREFOX:
                self.driver = webdriver.Firefox()
            elif browser_type == BrowserType.CHROME:
                self.driver = webdriver.Chrome()
            elif browser_type == BrowserType.IE:
                self.driver = webdriver.Ie()
            else:
                self.driver = None

            self.driver.maximize_window()
            self.driver.delete_all_cookies()
            self.implicitly_wait(5)
            self.set_page_load_timeout(5)
            print(GM.SELECTED_OPENED)

    def get_title(self):
        return self.driver.title

    def get_driver(self):
        return self

    def get(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def find_element(self, by=By.ID, value=None):
        return self.driver.find_element(by, value)

    def find_elements(self, by=By.ID, value=None):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        we = self.find_element(by, value)
        we.click()

    def get_attribute(self, by, value, attribute):
        we = self.find_element(by, value)
        we.get_attribute(attribute)

    def is_displayed(self, by, value):
        we = self.find_element(by, value)
        return we.is_displayed()

    def is_enabled(self, by, value):
        we = self.find_element(by, value)
        return we.is_enabled()

    def send_keys(self, by, value, word):
        we = self.find_element(by, value)
        we.send_keys(word)

    def get_element_text(self, by, value):
        we = self.find_element(by, value)
        return we.text
        #return we.get_attribute('text') CHECK THIS



    def set_combo_option(self, by, value, option):
        we = Select(self.find_element(by, value))
        we.select_by_visible_text(option)

    # WAIT METHODS

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def set_page_load_timeout(self, seconds):
        self.driver.set_page_load_timeout(seconds)

    def wait_for_element_present(self, by, value, seconds):
        try:
            element = WebDriverWait(self.driver, seconds).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            element = None
        return element

    def wait_for_element_visible(self, by, value, seconds):
        try:
            element = WebDriverWait(self.driver, seconds).until(
                EC.visibility_of_element_located((by, value)))
        except TimeoutException:
            element = None
        return element

    def wait_for_title_present(self, title, seconds):
        try:
            is_present = WebDriverWait(self.driver, seconds).until(
                EC.title_is(title))
        except TimeoutException:
            is_present = False
        return is_present

    def wait_for_title_contains(self, title, seconds):
        try:
            is_present = WebDriverWait(self.driver, seconds).until(
                EC.title_contains(title))
        except TimeoutException:
            is_present = False
        return is_present
