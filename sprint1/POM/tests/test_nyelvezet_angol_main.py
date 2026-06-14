import allure
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

from sprint1.POM.page_models.main_page_a import MoovSmartMain

URL = "http://localhost:4200"



class TestNyelvezetAngolMain:

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
    def test_nyelvezet_angol_main(self):

        home_page = MoovSmartMain(self.browser, URL) #meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")

        assert home_page.get_buy().text == "Buy" # ellenőrizzük, hogy a "buy" gombon "Buy" felirat van-e
        assert home_page.rent_button().text == "Rent"
        assert home_page.sing_in_button().text == "Sign In"
        assert home_page.registration_button().text == "Registration"
        assert home_page.get_search_placeholder() == "Enter the city"