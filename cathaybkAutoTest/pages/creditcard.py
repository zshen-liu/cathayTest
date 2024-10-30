from .base_page import BasePage
from selenium.webdriver.common.by import By
import logging


class CreditCard(BasePage):
    def __init__(self, url: str, driver):
        super().__init__(url, driver)
        self.apply_credit_loc = (By.LINK_TEXT, '申請信用卡')
        self.credit_card_list_loc = (By.XPATH, "//div[text()='信用卡']//following-sibling::a")

    def click_apply_credit(self):
        self.wait_element(self.apply_credit_loc)
        self.driver.find_element(*self.apply_credit_loc).click()

    def record_all_credit_card_item(self):
        self.wait_element(self.credit_card_list_loc)
        sub_item = self.driver.find_elements(*self.credit_card_list_loc)
        for item in sub_item:
            logging.info(f'credit card item is {item.text}')
