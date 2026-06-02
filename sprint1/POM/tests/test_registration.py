import pytest
import allure
import time

from sprint1.POM.page_models.main_page_z import MoovSmartMain
from sprint1.POM.page_models.registration_page_z import RegistrationPage
from sprint1.POM.page_models.login_page_z import LoginPage
from sprint1.POM.page_models.logged_in_page_z import LoggedIn
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.testdata.testuser_reg import TESTUSER
from sprint1.POM.testdata.testurls import BASE_URL

class TestRegistration:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)

    def teardown_method(self):
        self.main_page.close_browser()

    @allure.title("Regisztráció magyar felületen - valid")
    @allure.description("Regisztráció - pozitív")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration_hun_valid(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[0]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[0]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[0]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[0]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[0]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[0]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[0]["password_confirm"])
        # self.registration_page.button_registration().click()
        button = self.registration_page.button_registration()
        self.browser.execute_script("arguments[0].click();", button)
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/"

    @allure.title("Regisztráció magyar felületen - ugyanazzal az email címmel")
    @allure.description("Regisztráció - negatív")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration_hun_with_same_email(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[0]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[0]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[0]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[0]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[0]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[0]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[0]["password_confirm"])
        # self.registration_page.button_registration().click()
        button = self.registration_page.button_registration()
        self.browser.execute_script("arguments[0].click();", button)
        assert self.registration_page.error_email_missing().is_displayed()
        real_error = self.registration_page.error_email_missing()
        real_error_text =real_error.text
        assert real_error_text == "Email address is already taken!"

    @allure.title("Regisztráció magyar felületen - nem megfelelő névvel és telefonszámmal")
    @allure.description("Regisztráció - negatív")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration_hun_with_invalid_name_and_phone(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[1]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[1]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[1]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[1]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[1]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[1]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[1]["password_confirm"])
        # self.registration_page.button_registration().click()
        button = self.registration_page.button_registration()
        self.browser.execute_script("arguments[0].click();", button)
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/"

    @allure.title("Regisztráció magyar felületen - nem megfelelő email címmel")
    @allure.description("Regisztráció - negatív")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration_hun_with_invalid_email(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[2]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[2]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[2]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[2]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[2]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[2]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[2]["password_confirm"])
        # self.registration_page.button_registration().click()
        # button = self.registration_page.button_registration()
        # self.browser.execute_script("arguments[0].click();", button)
        real_error = self.registration_page.error_email_missing()
        real_error_text = real_error.text
        assert real_error_text == "Hibásan kitöltött mező!"



    # def test_registration_hun_with_wrong_lastname(self):
    #     pass
    #
    # def test_registration_hun_with_wrong_firstname(self):
    #     pass
    #
    # def test_registration_hun_with_wrong_phone_number(self):
    #     pass
    #
    # def test_registration_hun_with_wrong_password(self):
    #     pass
    #
    # def test_registration_hun_with_wrong_password_confirm(self):
    #     pass


