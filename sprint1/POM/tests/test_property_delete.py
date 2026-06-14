import pytest
import allure

from sprint1.POM.page_models.main_page import MoovSmartMain
from sprint1.POM.page_models.registration_page import RegistrationPage
from sprint1.POM.page_models.login_page import LoginPage
from sprint1.POM.page_models.logged_in_page import LoggedIn
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.testdata.testurls import BASE_URL
from sprint1.POM.page_models.login_page_ma import LoginPage
from sprint1.POM.page_models.logged_in_page_ma import LoggedIn
from sprint1.POM.page_models.my_properties_page_ma import MyProperties


class TestPropertyDelete:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)
        self.login_page_ma = LoginPage(self.browser, BASE_URL)
        self.logged_in_page_ma = LoggedIn(self.browser, BASE_URL)
        self.my_properties_page_ma = MyProperties(self.browser, BASE_URL)

        # Minden teszt ezekkel a lépésekkel indul, így ideális itt futtatni őket
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.login().click()

    def teardown_method(self):
        self.main_page.close_browser()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password,property_address, title, description, tag",
        [
            ("test3@test.hu", "1234_Abcd", "7100 Szekszárd, Kossuth Lajos street", "Property delete eng tc01",
             "Delete a property",
             ["All good", "No error", "Success"])
        ]
    )
    def test_property_delete(self, email, password, property_address, title, description, tag):
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_delete_on_property(property_address)
        self.my_properties_page_ma.click_confirm_delete(property_address)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password,property_address, title, description, tag",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "Property delete cancel eng tc02",
             "Delete cancel at a property",
             ["All good", "No error", "Success"])
        ]
    )
    def test_property_cancel_delete(self, email, password, property_address, title, description, tag):
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_delete_on_property(property_address)
        self.my_properties_page_ma.click_cancel_delete(property_address)
