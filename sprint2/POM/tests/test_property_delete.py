import time

import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sprint2.POM.page_models.main_page import MoovSmartMain
from sprint2.POM.page_models.registration_page import RegistrationPage
from sprint2.POM.page_models.login_page import LoginPage
from sprint2.POM.page_models.logged_in_page import LoggedIn
from sprint2.POM.page_models.my_properties_page import MyProperties
from sprint2.POM.create_driver import get_configured_chrome_driver
from sprint2.POM.testdata.testurls import BASE_URL


class TestPropertyDelete:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)
        self.my_properties_page_ma = MyProperties(self.browser, BASE_URL)

        # Minden teszt ezekkel a lépésekkel indul, így ideális itt futtatni őket
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.login().click()

    def teardown_method(self):
        self.main_page.close_browser()

    @allure.title("TC01 - Ingatlan törlés.")
    @allure.tag( "Functional", "Property delete")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, property_address, description",
        [
            ("test3@test.hu", "1234_Abcd", "1161 Budapest, Sándor street", "Property delete")
        ]
    )
    def test_property_delete(self, email, password, property_address, description):
        self.login_page._execute_login(email, password)
        self.logged_in_page.navigate_to_my_properties()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.my_properties_page_ma.property_cards)
        )
        # 1. Lekérjük a törlés előtti lista hosszát
        initial_properties = self.my_properties_page_ma.get_property_list_elements()
        initial_count = len(initial_properties)
        # 2. Elvégezzük a törlést
        self.my_properties_page_ma.click_delete_on_property(property_address)
        self.my_properties_page_ma.click_confirm_delete(property_address)
        # Várunk, hogy a frontend frissítse a listát (eltűnjön a törölt elem)
        time.sleep(0.8)
        # 3. Lekérjük a törlés utáni lista hosszát
        after_delete_properties = self.my_properties_page_ma.get_property_list_elements()
        after_delete_count = len(after_delete_properties)

        # 4. Assert: A darabszámnak pontosan eggyel kevesebbnek kell lennie
        assert after_delete_count == initial_count - 1, (
            f"BUG: A lista hossza nem csökkent! "
            f"Eredeti darabszám: {initial_count}, Törlés utáni darabszám: {after_delete_count}"
        )

    @allure.title("TC02 - Ingatlan törlésének visszavonása.")
    @allure.tag( "Functional", "Property delete")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, property_address, description",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "Property delete cancel",)
        ]
    )
    def test_property_cancel_delete(self, email, password, property_address, description):
        self.login_page._execute_login(email, password)
        self.logged_in_page.navigate_to_my_properties()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.my_properties_page_ma.property_cards)
        )
        # 1. Lekérjük a kiinduló lista hosszát
        initial_properties = self.my_properties_page_ma.get_property_list_elements()
        initial_count = len(initial_properties)
        # 2. Megnyitjuk a törlést, majd a Mégse gombra kattintunk
        self.my_properties_page_ma.click_delete_on_property(property_address)
        self.my_properties_page_ma.click_cancel_delete(property_address)
        time.sleep(0.5)
        # 3. Lekérjük a hosszát a visszavonás után is
        after_cancel_properties = self.my_properties_page_ma.get_property_list_elements()
        after_cancel_count = len(after_cancel_properties)

        # 4. Assert: A darabszámnak meg kell egyeznie az eredetivel
        assert after_cancel_count == initial_count, (
            f"BUG: A lista hossza megváltozott a törlés visszavonása után! "
            f"Eredeti: {initial_count}, Visszavonás után: {after_cancel_count}"
        )
