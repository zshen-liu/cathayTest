import pytest
from ..pages.login_page import LoginPage
from ..pages.menu_page import MenuPage
from ..pages.product_list import ProductList
from ..pages.creditcard import CreditCard
from ..pages.online_apply_credit_card import OnlineApplyCreditCard
from .utils.menu_type import MenuType
from .utils.personal_sub_type import PersonFinSubType
from .utils.product_sub_type import ProductSubType
from .utils.online_credit_card_type import OnlineCardType


@pytest.mark.usefixtures("set_config_from_cmd", "browser")
class TestCathay:
    def test_apply_credit_flow(self, set_config_from_cmd, browser):
        url = set_config_from_cmd.url
        login_page = LoginPage(url, browser)
        login_page.open()
        login_page.screen_shot('login.png')
        # click more menu
        login_page.click_menu()

        menu_page = MenuPage(url, browser)
        menu_list = menu_page.get_menu_list()

        check_menu = MenuType.MenuList

        assert len(menu_list) == len(check_menu)
        for menu in check_menu:
            assert menu in menu_list

        menu_page.screen_shot('menu.png')

        menu_page.click_sub_product(PersonFinSubType.ProductIntro)

        product_list = ProductList(url, browser)

        product_list.screen_shot('product.png')

        product_list.click_product_item(ProductSubType.Credit)

        credit_card = CreditCard(url, browser)
        # log all credit sub item
        credit_card.record_all_credit_card_item()
        credit_card.screen_shot('credit_sub_item.png')
        # To apply credit card
        credit_card.click_apply_credit()

        online_apply_credit_card = OnlineApplyCreditCard(url, browser)

        assert online_apply_credit_card.get_tittle() == OnlineCardType.Tittle
        online_apply_credit_card.screen_shot('apply_credit_card.png')
        # To get all card type number
        card_type_total = online_apply_credit_card.get_card_list_total()

        for i in range(card_type_total):
            online_apply_credit_card.screen_shot(f'card_type{i}.png')
            online_apply_credit_card.click_next_switch_card()
        # switch to card type to  全部
        while online_apply_credit_card.get_current_card() != OnlineCardType.All:
            online_apply_credit_card.click_next_switch_card()

        for i in range(9):
            online_apply_credit_card.screen_shot(f'online_card_{i}.png')
            online_apply_credit_card.scroll_all_card()
