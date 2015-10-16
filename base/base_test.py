from unittest import TestCase

from configs.base_framework_configs import GlobalConfigs as GC
from driver.action_bot import ActionBot

class BaseTest(TestCase):
    def setUp(self):
        self.action_bot = ActionBot(GC.BROWSER)
        self.driver = self.action_bot.get_driver()
        self.url = GC.URL
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()
