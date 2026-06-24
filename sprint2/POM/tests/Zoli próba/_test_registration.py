import pytest
import allure
import time

from sprint1.POM.page_models.main_page import MoovSmartMain
from sprint1.POM.page_models.registration_page import RegistrationPage
from sprint1.POM.page_models.login_page import LoginPage
from sprint1.POM.page_models.logged_in_page import LoggedIn
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

    # def teardown_method(self):
    #     self.main_page.close_browser()

    @allure.title("Registration eng tc01")
    @allure.description("Registration - valid")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Valid registration")
    def test_registration_eng_valid(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[0]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[0]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[0]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[0]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[0]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[0]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[0]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/"

    @allure.title("Registration eng tc02")
    @allure.description("Registration with same email")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - same email")
    def test_registration_eng_with_same_email(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[0]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[0]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[0]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[0]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[0]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[0]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[0]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.registration_page.error_email_missing_or_wrong_single().is_displayed()
        assert self.registration_page.error_email_missing_or_wrong_single().text == "Email address is already taken!"
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc03")
    @allure.description("Registration without last name")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - last name empty")
    def test_registration_eng_without_lastname(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[1]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[1]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[1]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[1]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[1]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[1]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[1]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.registration_page.error_last_name().is_displayed()
        assert self.registration_page.error_last_name().text == "Please enter your last name"
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc04")
    @allure.description("Registration without first name")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - first name empty")
    def test_registration_eng_without_firstname(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[2]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[2]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[2]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[2]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[2]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[2]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[2]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.registration_page.error_first_name().is_displayed()
        assert self.registration_page.error_first_name().text == "Please enter your first name"
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc05")
    @allure.description("Registration without phone number")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - phone number empty", "Phone number - Not required", "Can be empty")
    def test_registration_eng_without_phone_number(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[3]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[3]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[3]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[3]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[3]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[3]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[3]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert not self.registration_page.error_phone_number().is_displayed()
        assert self.browser.current_url == "http://localhost:4200/"

    @allure.title("Registration eng tc06")
    @allure.description("Registration with invalid names and phone number")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - numbers in name", "Registration - letters in phone number")
    def test_registration_eng_with_invalid_names_and_phone(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[4]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[4]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[4]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[4]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[4]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[4]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[4]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc07")
    @allure.description("Registration with invalid email")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - invalid email")
    def test_registration_eng_with_invalid_email(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[5]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[5]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[5]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[5]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[5]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[5]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[5]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.registration_page.error_email_missing_or_wrong_single().is_displayed()
        assert self.registration_page.error_email_missing_or_wrong_single().text == "Not a proper email format!"
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc08")
    @allure.description("Registration with wrong email confirmation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - wrong email confirmation", "typo")
    def test_registration_eng_with_wrong_email_confirm(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[6]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[6]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[6]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[6]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[6]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[6]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[6]["password_confirm"])
        assert self.registration_page.error_confirm_email().is_displayed()
        assert self.registration_page.error_confirm_email().text == "Email does not match"
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/registration-form"

    @allure.title("Registration eng tc09")
    @allure.description("Registration with wrong password")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - wrong password")
    def test_registration_eng_with_wrong_password(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[7]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[7]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[7]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[7]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[7]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[7]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[7]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.registration_page.error_password().is_displayed()
        assert self.registration_page.error_password().text == "Please enter a password"
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc10")
    @allure.description("Registration with wrong password confirmation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - wrong password confirmation", "typo")
    def test_registration_eng_with_wrong_password_confirm(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[8]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[8]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[8]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[8]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[8]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[8]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[8]["password_confirm"])
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.registration_page.error_confirm_password().is_displayed()
        assert self.registration_page.error_confirm_password().text == "Password does not match"
        assert self.browser.current_url != "http://localhost:4200/"

    @allure.title("Registration eng tc11")
    @allure.description("Registration with wrong email & password confirmation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Registration - wrong email & password confirmation", "typo")
    def test_registration_eng_with_wrong_email_and_password_confirm(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()
        self.registration_page.last_name().send_keys(TESTUSER[9]["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER[9]["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER[9]["phone_number"])
        self.registration_page.email().send_keys(TESTUSER[9]["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER[9]["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER[9]["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER[9]["password_confirm"])
        assert self.registration_page.error_confirm_email().is_displayed()
        assert self.registration_page.error_confirm_email().text == "Email does not match"
        registration_text = self.registration_page.registration_text()
        registration_text.click()
        assert self.registration_page.error_confirm_password().is_displayed()
        assert self.registration_page.error_confirm_password().text == "Password does not match"
        button = self.registration_page.button_registration()
        # Legörgetünk a gombhoz, hogy láthatóvá váljon
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Kis biztonsági várakozás, amíg a görgetési animáció lefut
        time.sleep(0.5)
        # Most már biztonságosan kattinthatunk
        button.click()
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/registration-form"


