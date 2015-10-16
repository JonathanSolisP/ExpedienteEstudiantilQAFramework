from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from configs.base_framework_configs import GlobalConfigsMessages as GM

from selenium import webdriver
from driver.browser_type import BrowserType as BrowserType

class ActionBot():
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

            self.implicitly_wait(2)

            self.set_page_load_timeout(5)
            print(GM.SELECTED_OPENED)

    def get_title(self):
        return self.driver.title

    def get_driver(self):
        """
        Gets the driver object which is a instance of itself

        :return: ActionBot object
        """
        return self

    def get(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    # WAIT METHODS

    def implicitly_wait(self, seconds):
        """
        Sets a sticky timeout to implicitly wait for an element to be found,
        or a command to complete.
        This method only needs to be called one time per session. To set the
        timeout for calls to execute_async_script, see set_script_timeout.

        :param seconds: number of seconds to wait
        """
        self.driver.implicitly_wait(seconds)

    def set_page_load_timeout(self, seconds):
        """
        Set the amount of time to wait for a page load to complete
        before throwing an error.

        :param seconds: Number of seconds to wait
        """
        self.driver.set_page_load_timeout(seconds)
