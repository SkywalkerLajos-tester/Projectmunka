import allure
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

from sprint1.POM.page_models.main_page_a import MoovSmartMain

URL = "http://localhost:4200"


class TestLanguageEnglish:

    def setup_method(self):
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_argument('--guest')
        options.add_argument("lang=hu")  # hu (magyar) vagy en (angol), böngésző nyelve
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.close()

    @allure.title("Nyelv egyesítése  főoldalon")
    @allure.description("Angol")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_language_english_main(self):
        home_page = MoovSmartMain(self.browser, URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")

        assert home_page.get_buy().text == "Buy"  # ellenőrizzük, hogy a "buy" gombon "Buy" felirat van-e
        assert home_page.rent_button().text == "Rent"
        assert home_page.sing_in_button().text == "Sign In"
        assert home_page.registration_button().text == "Registration"
        assert home_page.get_search_placeholder() == "Enter the city"

    @allure.title("Nyelv egyesítése a regisztráció oldalán")
    @allure.description("Angol")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_lanuage_english_registration(self):
        home_page = MoovSmartMain(self.browser, URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")
        home_page.registration_button().click()

        assert home_page.registration_word().text == "Registration"
        assert home_page.last_name_word().text == "Last name:"
        assert home_page.first_name_word().text == "First name:"
        assert home_page.phone_number_word().text == "Phone number:"
        assert home_page.email_address_word().text == "Email address"
        assert home_page.email_address_again_word().text == 'Email address again:'
        assert home_page.plaese_enter_a_password_word().text == 'Please enter a password:'
        assert home_page.please_enter_a_password_again_word().text == 'Please enter a password again:'
        assert home_page.register_button().text == 'Register'

    @allure.title("Nyelv egyesítése  egyéb oldalon")
    @allure.description("Angol")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_language_english_sign_in(self):
        home_page = MoovSmartMain(self.browser, URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")
        home_page.sing_in_button().click()

        assert home_page.email().text == "Email address"  # ellenőrizzük, hogy ahova az e-mail címet kell beírni ott "Email address" felirat van-e
        assert home_page.password().text == "Password"
        assert home_page.sing_in_button().text == "Sign In"
        assert home_page.text_center().text == "Don't have an account yet? Register now!"
