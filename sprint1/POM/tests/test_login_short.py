import pytest
import allure

from sprint1.POM.page_models.main_page_z import MoovSmartMain
from sprint1.POM.page_models.registration_page_z import RegistrationPage
from sprint1.POM.page_models.login_page_z import LoginPage
from sprint1.POM.page_models.logged_in_page_z import LoggedIn
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.testdata.testurls import BASE_URL


class TestLogin:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)

        # Minden teszt ezekkel a lépésekkel indul, így ideális itt futtatni őket
        self.main_page.open_webpage()
        self.main_page.select_language_hu()
        self.main_page.login().click()

    def teardown_method(self):
        self.main_page.close_browser()

    def _execute_login(self, email, password):
        """Közös segédmetódus az adatok beírására és a kattintásra."""
        self.login_page.email_address().send_keys(email)
        self.login_page.enter_password().send_keys(password)
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)

    @allure.title("Bejelentkezés valid")
    @allure.description("Bejelentkezés - happy path")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        self._execute_login("test1@test.hu", "1234_Abcd")

        signed_in_text = self.logged_in_page.button_exit().text
        assert signed_in_text == "Kijelentkezés"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, title, description",
        [
            ("", "1234_Abcd", "Email nélkül", "Bejelentkezés - email cím megadása nélkül"),
            ("test1@test.hu", "", "Jelszó nélkül", "Bejelentkezés - jelszó megadása nélkül"),
            ("te1st1@test.hu", "1234_Abcd", "Hibás email", "Bejelentkezés - rossz email címmel"),
            ("test1@test.hu", "1234_Abc", "Hibás jelszó", "Bejelentkezés - rossz jelszóval"),
        ]
    )
    def test_login_invalid_cases(self, email, password, title, description):
        """A 4 negatív teszteset összevonva, dinamikus Allure megnevezésekkel."""
        allure.dynamic.title(f"Bejelentkezés hiba: {title}")
        allure.dynamic.description(description)

        self._execute_login(email, password)

        assert self.login_page.error_message().is_displayed()