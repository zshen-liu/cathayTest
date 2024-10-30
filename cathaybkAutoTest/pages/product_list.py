import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class ProductList(BasePage):

    def __init__(self, url: str, driver):
        super().__init__(url, driver)
        self.product_list_loc = (By.XPATH, '//div[@class="cubre-a-menuSortBtn"]')

    def click_product_item(self, product_name):
        try:
            product_items = self.driver.find_elements(*self.product_list_loc)
            for item in product_items:
                if product_name in item.text:
                    item.click()
                    break
        except TimeoutException as e:
            raise e

    def get_product_present(self):
        self.wait_element(self.product_list_loc)
        product_items = self.driver.find_elements(*self.product_list_loc)
        product_name = [item.text for item in product_items]
        return product_name
