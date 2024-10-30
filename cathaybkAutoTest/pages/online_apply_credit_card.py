from .base_page import BasePage
from selenium.webdriver.common.by import By


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
        self.wait_element(self.next_button_loc)
        self.driver.find_element(*self.next_button_loc).click()

    def get_tittle(self):
        self.wait_element(self.online_apply_card_page_title_loc)
        title = self.driver.find_element(*self.online_apply_card_page_title_loc)
        return title.text

    def get_card_list_total(self):
        self.wait_element(self.card_type_list_loc)
        card_list = self.driver.find_elements(*self.card_type_list_loc)
        return len(card_list)

    def get_current_card(self):
        self.wait_element(self.current_card_loc)
        current_card = self.driver.find_element(*self.current_card_loc)
        return current_card.text

    def scroll_all_card(self):
        self.driver.execute_script("window.scrollBy(150, 300)")
