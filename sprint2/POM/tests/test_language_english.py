import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from sprint1.POM.page_models.main_page_a import MoovSmartMain
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.testdata.testurls import BASE_URL



class TestLanguageEnglish:

    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page_a = MoovSmartMain(self.browser, BASE_URL)
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.main_page.open_webpage()


    def teardown_method(self):
        self.browser.close()

    @allure.title("Nyelv egységesítése a főoldalon")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Language - English", "Read")

    def test_language_english_main(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")

        assert home_page.get_buy().text == "Buy"  # ellenőrizzük, hogy a "buy" gombon "Buy" felirat van-e
        assert home_page.rent_button().text == "Rent"
        assert home_page.sing_in_button().text == "Sign In"
        assert home_page.registration_button().text == "Registration"
        assert home_page.header_title().text == "Find your new community today"
        assert home_page.get_search_placeholder() == "Enter the city"
        assert home_page.main_header_title_sale().text == "Recent properties for Sale"
        assert home_page.main_header_title_rent().text == "Recent properties for Rent"

    @allure.title("Nyelv egységesítése az eladó oldalon")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Language - English", "Read")
    def test_language_english_buy(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")
        home_page.get_buy().click()

        home_page.for_sale_button().click()
        assert home_page.for_sale_button().text == "For Sale\nFor Rent"
        assert home_page.city_placeholder().get_attribute("placeholder") == "City"
        assert home_page.search_button().text == "Search"

    @allure.title("Nyelv egységesítése a kiadó oldalon")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Language - English", "Read")
    def test_language_english_rent(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")
        home_page.rent_button().click()

        home_page.for_sale_button().click()
        assert home_page.for_sale_button().text == "For Sale\nFor Rent"
        assert home_page.city_placeholder().get_attribute("placeholder") == "City"
        assert home_page.search_button().text == "Search"

    @allure.title("Nyelv egységesítése a bejelentkezés oldalon")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Language - English", "Read")
    def test_language_english_sign_in(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")
        home_page.sing_in_button().click()

        assert home_page.email().text == "Email address"  # ellenőrizzük, hogy ahova az e-mail címet kell beírni ott "Email address" felirat van-e
        assert home_page.password().text == "Password"
        assert home_page.sing_in_button().text == "Sign In"
        assert home_page.text_center().text == "Don't have an account yet? Register now!"

    @allure.title("Nyelv egységesítése a regisztráció oldalán")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Language - English", "Read")
    def test_lanuage_english_registration(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
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
