import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    def __init__(self, url: str, driver):
        self.url = url
        self.driver = driver

    def open(self):
        self._open(self.url)

    def _open(self, url: str):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def screen_shot(self, file_name: str):
        try:
            WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(1)
            screenshot_folder = "screenshots"

            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)
            screenshot_path = os.path.join(screenshot_folder, file_name)
            if os.path.exists(screenshot_path):
                os.remove(screenshot_path)
            self.driver.save_screenshot(screenshot_path)

        except TimeoutException as e:
            raise e
