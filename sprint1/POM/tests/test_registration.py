import time


from sprint1.POM.page_models.main_page import MoovSmartMain
from sprint1.POM.page_models.registration_page import RegistrationPage
from sprint1.POM.page_models.login_page import LoginPage
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.general_page import GeneralPage
from sprint1.POM.testdata.testuser_reg import TESTUSER
from sprint1.POM.testdata.testurls import BASE_URL

class TestRegistration:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)

    # def teardown_method(self):
    #     self.main_page.close_browser()

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
        self.registration_page.button_registration().click()
        assert login_page.sign_in_window is displayed

    def test_registration_hun_with_same_email(self):
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
        #self.registration_page.button_registration().click()

    def test_registration_hun_with_wrong_email(self):
        pass

    def test_registration_hun_with_wrong_email_confirm(self):
        pass

    def test_registration_hun_with_wrong_lastname(self):
        pass

    def test_registration_hun_with_wrong_firstname(self):
        pass

    def test_registration_hun_with_wrong_phone_number(self):
        pass

    def test_registration_hun_with_wrong_password(self):
        pass

    def test_registration_hun_with_wrong_password_confirm(self):
        pass


