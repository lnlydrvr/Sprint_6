import allure
import src.data as data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage

@allure.suite('Тесты переходов по ссылкам в верхнем меню')
class TestTransitionPage:
    @allure.title('Переход на страницу главную страницу по логотипу "Самоката"')
    def test_transition_by_scooter_logo(self, driver):
        MainPage(driver).go_to_order_page()
        assert OrderPage(driver).get_user_info_header().text == data.order_form_user_info_header_text

        RedirectPage(driver).go_to_main_page_by_scooter_logo()
        assert data.scooter_header in MainPage(driver).get_main_header_text()

    @allure.title('Переход на страницу Дзен по логотипу "Яндекс"')
    def test_transition_by_yandex_logo(self, driver):
        RedirectPage(driver).go_to_dzen_by_yandex_logo()
        assert RedirectPage(driver).get_dzen_news_text() == data.dzen_header