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

        # Minden teszt ezekkel a lépésekkel indul, így ideális itt futtatni őket
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.login().click()

    def teardown_method(self):
        self.main_page.close_browser()

    def _execute_login(self, email, password):
        """Közös segédmetódus az adatok beírására és a kattintásra."""
        self.login_page.email_address().send_keys(email)
        self.login_page.enter_password().send_keys(password)
        button = self.login_page.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, title, description, tag",
        [
            ("test1@test.hu", "1234_Abcd", "Login eng tc01", "Login valid - happy path", ["All good", "No error", "Success"])
        ]
    )
    def test_login_valid(self, email, password, title, description, tag):
        allure.dynamic.title(title)
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self._execute_login("test1@test.hu", "1234_Abcd")
        self._execute_login(email, password)

        signed_in_text = self.logged_in_page.button_exit().text
        assert signed_in_text == "Logout"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, title, description, tag",
        [
            ("", "1234_Abcd", "Login eng tc02", "Login without email", ["Invalid login", "Without email", "Missing error message", "Please enter an email"]),
            ("test1@test.hu", "", "Login eng tc03", "Login without password", ["Invalid login", "Without password"]),
            ("te1st1@test.hu", "1234_Abcd", "Login eng tc04", "Login with wrong email", ["Invalid login", "With wrong email"]),
            ("test1@test.hu", "1234_Abc", "Login eng tc05", "Login with wrong password", ["Invalid login", "With wrong password"]),
        ]
    )
    def test_login_invalid_cases(self, email, password, title, description, tag):
        """A 4 negatív teszteset összevonva, dinamikus Allure megnevezésekkel."""
        allure.dynamic.title(title)
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self._execute_login(email, password)

        assert self.login_page.error_message().is_displayed(), "A hibaüzenet nem jelent meg a képernyőn!"
