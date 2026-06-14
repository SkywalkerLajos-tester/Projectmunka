
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from sprint1.POM.page_models.main_page_a import MoovSmartMain

URL = "http://localhost:4200"

class TestNyelvezetAngolSignIn:


    def setup_method(self):
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_argument('--guest')
        options.add_argument("lang=hu")  # hu (magyar) vagy en (angol), böngésző nyelve
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.close()


    @allure.title("Nyelv egyesítése  egyéb oldalon")
    @allure.description("Angol")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_nyelvezet_angol_sign_in(self):

        home_page = MoovSmartMain(self.browser, URL) #meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("English")
        home_page.sing_in_button().click()

        assert home_page.email().text == "Email address"  # ellenőrizzük, hogy ahova az e-mail címet kell beírni ott "Email address" felirat van-e
        assert home_page.password().text == "Password"
        assert home_page.sing_in_button().text == "Sign In"
        assert home_page.text_center().text ==  "Don't have an account yet? Register now!"