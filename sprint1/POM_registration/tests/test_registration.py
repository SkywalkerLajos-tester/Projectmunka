import time

from sprint1.POM_registration.page_models.main_page import MoovSmartMain
from sprint1.POM_registration.page_models.registration_page import RegistrationPage
from sprint1.POM_registration.create_driver import get_configured_chrome_driver
from sprint1.POM_registration.general_page import GeneralPage
from sprint1.POM_registration.testdata.testuser import TESTUSER
from sprint1.POM_registration.testdata.testurls import BASE_URL

class TestRegistration:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)

    # def teardown_method(self):
    #     self.main_page.close_browser()

    def test_registration_hun(self):
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration_en().click()
        self.registration_page.last_name().send_keys(TESTUSER["lastname"])
        self.registration_page.first_name().send_keys(TESTUSER["firstname"])
        self.registration_page.phone_number().send_keys(TESTUSER["phone_number"])
        self.registration_page.email().send_keys(TESTUSER["email"])
        self.registration_page.confirm_email().send_keys(TESTUSER["email_confirm"])
        self.registration_page.password().send_keys(TESTUSER["password"])
        self.registration_page.confirm_password().send_keys(TESTUSER["password_confirm"])
        #self.registration_page.button_registration().click()


