from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, url: str, driver):
        super().__init__(url, driver)
        self.is_load_loc = (By.XPATH, '//h1[text()="每次都是更好的體驗"]')
        self.menu_loc = (By.CLASS_NAME, 'cubre-o-header__burger')

    def open(self):
        super().open()

    def click_menu(self):
        self.wait_element(self.menu_loc)
        self.driver.find_element(*self.menu_loc).click()
