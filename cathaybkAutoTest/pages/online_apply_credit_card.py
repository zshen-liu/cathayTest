from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OnlineApplyCreditCard(BasePage):
    def __init__(self, url: str, driver):
        super().__init__(url, driver)
        self.next_button_loc = (By.CLASS_NAME, 'bx-next')
        self.online_apply_card_page_title_loc = (By.XPATH, '//div[contains(text(), "線上申辦信用卡")]')
        self.card_type_list_loc = (
            By.XPATH, '//div[contains(text(), "請選擇卡片")]//following::div[contains(@class, "bx-pager-item")]')
        self.current_card_loc = (
            By.XPATH, '//div[@class="slider"]//following::li[contains(@aria-hidden, "false")]//following::a')

    def click_next_switch_card(self):
        try:
            WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.next_button_loc)))
            self.driver.find_element(*self.next_button_loc).click()
        except TimeoutException as e:
            raise e

    def get_tittle(self):
        try:
            WebDriverWait(self.driver, 10).until(
                (EC.visibility_of_element_located(self.online_apply_card_page_title_loc)))
            title = self.driver.find_element(*self.online_apply_card_page_title_loc)
            return title.text
        except TimeoutException as e:
            raise e

    def get_card_list_total(self):
        try:
            WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.card_type_list_loc)))
            card_list = self.driver.find_elements(*self.card_type_list_loc)
            return len(card_list)
        except TimeoutException as e:
            raise e

    def get_current_card(self):
        try:
            WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.current_card_loc)))
            current_card = self.driver.find_element(*self.current_card_loc)
            return current_card.text
        except TimeoutException as e:
            raise e

    def scroll_all_card(self):
        self.driver.execute_script("window.scrollBy(150, 300)")
