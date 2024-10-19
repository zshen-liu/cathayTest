from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MenuPage(BasePage):
    def __init__(self, url: str, driver):
        super().__init__(url, driver)
        self.menu_list_loc = (
            By.XPATH, '//div[@class="cubre-o-channel"]//following::div[@class="cubre-o-channel__item"]')
        self.person_finance_loc = (By.CLASS_NAME, 'cubre-a-menuLink -channel is-active')
        self.personal_final_loc_list = (
            By.XPATH, '//div[@class="cubre-o-menu__btn"]//following::div[@class="cubre-o-menu__btn"]')

    def get_menu_list(self):
        try:
            WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.menu_list_loc)))
            menu_list = self.driver.find_elements(*self.menu_list_loc)
            menu_name_list = [menu.text for menu in menu_list]
            return menu_name_list
        except TimeoutException as e:
            raise e

    def click_person_finance(self, screen_shot_flag=False, file_name=None):
        try:
            WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.person_finance_loc)))
            self.driver.find_element(*self.person_finance_loc).click()
        except TimeoutException as e:
            raise e

    def click_sub_product(self, sub_type):
        try:
            WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.personal_final_loc_list)))
            personal_sub_list = self.driver.find_elements(*self.personal_final_loc_list)
            for item in personal_sub_list:
                if sub_type in item.text:
                    item.click()
                    break
        except TimeoutException as e:
            raise e
