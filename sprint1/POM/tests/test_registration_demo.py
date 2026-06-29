import pytest
import allure
import json
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

        # Minden teszt ezzel kezdődik
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()

    def teardown_method(self):
        self.main_page.close_browser()


    def fill_registration_form_and_submit(self, user_data, click_submit=True):
        """Helper metódus az űrlap kitöltéséhez és a beküldéshez."""
        allure.attach(json.dumps(user_data, indent=4, ensure_ascii=False),
            name="Felhasznált tesztadatok (TESTUSER)",
            attachment_type=allure.attachment_type.JSON)

        reg = self.registration_page

        reg.last_name().send_keys(user_data["lastname"])
        reg.first_name().send_keys(user_data["firstname"])
        reg.phone_number().send_keys(user_data["phone_number"])
        reg.email().send_keys(user_data["email"])
        reg.confirm_email().send_keys(user_data["email_confirm"])
        reg.password().send_keys(user_data["password"])
        reg.confirm_password().send_keys(user_data["password_confirm"])

        if click_submit:
            button = reg.button_registration()
            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(0.5)
            button.click()
            time.sleep(0.5)

# -------------------------------------------------------------------------
# TESZTESETEK
# -------------------------------------------------------------------------


    @allure.title("Registration eng tc01")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration - valid", ["Valid registration"])
        ]
    )
    def test_registration_eng_valid(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self.fill_registration_form_and_submit(TESTUSER[0])
        assert self.browser.current_url == "http://localhost:4200/"


    @allure.title("Registration eng tc05")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration without phone number",
             ["Registration - phone number empty", "Phone number - Not required", "Can be empty"])
        ]
    )
    def test_registration_eng_without_phone_number(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self.fill_registration_form_and_submit(TESTUSER[3])

        assert not self.registration_page.error_phone_number().is_displayed()
        assert self.browser.current_url == "http://localhost:4200/"


    @allure.title("Registration eng tc06")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with invalid names and phone number",
             ["Registration - numbers in names", "Registration - letters in phone number"])
        ]
    )
    def test_registration_eng_with_invalid_names_and_phone(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self.fill_registration_form_and_submit(TESTUSER[4])
        assert self.browser.current_url == "http://localhost:4200/registration-form"


    @allure.title("Registration eng tc08")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with wrong email confirmation", ["Registration - wrong email confirmation", "typo"])
        ]
    )
    def test_registration_eng_with_wrong_email_confirm(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # Itt még nem kattintunk, mert a gombnyomás előtt validálunk
        self.fill_registration_form_and_submit(TESTUSER[6], click_submit=False)

        error_msg = self.registration_page.error_confirm_email()
        assert error_msg.is_displayed()
        assert error_msg.text == "Email does not match"

        # Utólag rákattintunk, ahogy az eredeti tesztben volt
        button = self.registration_page.button_registration()
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        button.click()
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/registration-form"


    @allure.title("Registration eng tc11")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with wrong email & password confirmation",
             ["Registration - wrong email & password confirmation", "typo"])
        ]
    )
    def test_registration_eng_with_wrong_email_and_password_confirm(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self.fill_registration_form_and_submit(TESTUSER[9], click_submit=False)

        assert self.registration_page.error_confirm_email().is_displayed()
        assert self.registration_page.error_confirm_email().text == "Email does not match"

        self.registration_page.registration_text().click()

        assert self.registration_page.error_confirm_password().is_displayed()
        assert self.registration_page.error_confirm_password().text == "Password does not match"

        button = self.registration_page.button_registration()
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        button.click()
        time.sleep(0.5)
        assert self.browser.current_url == "http://localhost:4200/registration-form"

    @allure.title("Registration eng tc12")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with short names", ["Registration - short names", "Names too short", "Must be at least 3 characters long"])
        ]
    )
    def test_registration_eng_with_short_names(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self.fill_registration_form_and_submit(TESTUSER[10])

        assert self.browser.current_url != "http://localhost:4200/"
