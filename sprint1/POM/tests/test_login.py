import pytest
import allure

from sprint1.POM.page_models.main_page import MoovSmartMain
from sprint1.POM.page_models.registration_page import RegistrationPage
from sprint1.POM.page_models.login_page import LoginPage
from sprint1.POM.page_models.logged_in_page import LoggedIn
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.testdata.testurls import BASE_URL

class TestLogin:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)

    # def teardown_method(self):
    #     self.main_page.close_browser()

    @allure.title("Bejelentkezés tesztelése")
    @allure.description("Bejelentkezés - happy path")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.login().click()
        self.login_page.email_address().send_keys("test1@test.hu")
        self.login_page.enter_password().send_keys("1234_Abcd")
        # self.login_page.button_sign_in().click()
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)
        signed_in = self.logged_in_page.button_exit()
        signed_in_text = signed_in.text
        assert signed_in_text == "Kijelentkezés"

    @allure.title("Bejelentkezés tesztelése")
    @allure.description("Bejelentkezés - email cím megadása nélkül")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_without_email(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.login().click()
        self.login_page.email_address().send_keys("")
        self.login_page.enter_password().send_keys("1234_Abcd")
        # self.login_page.button_sign_in().click()
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)
        assert self.login_page.error_message().is_displayed()

    @allure.title("Bejelentkezés tesztelése")
    @allure.description("Bejelentkezés - jelszó megadása nélkül")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_without_password(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.login().click()
        self.login_page.email_address().send_keys("test1@test.hu")
        self.login_page.enter_password().send_keys("")
        # self.login_page.button_sign_in().click()
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)
        assert self.login_page.error_message().is_displayed()

    @allure.title("Bejelentkezés tesztelése")
    @allure.description("Bejelentkezés - rossz email címmel")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_wrong_email(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.login().click()
        self.login_page.email_address().send_keys("te1st1@test.hu")
        self.login_page.enter_password().send_keys("1234_Abcd")
        # self.login_page.button_sign_in().click()
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)
        assert self.login_page.error_message().is_displayed()

    @allure.title("Bejelentkezés tesztelése")
    @allure.description("Bejelentkezés - rossz jelszóval")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_wrong_password(self):
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.login().click()
        self.login_page.email_address().send_keys("test1@test.hu")
        self.login_page.enter_password().send_keys("1234_Abc")
        # self.login_page.button_sign_in().click()
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)
        assert self.login_page.error_message().is_displayed()
