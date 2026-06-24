import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sprint1.POM.page_models.base_page_a import BasePage
from sprint1.POM.page_models.main_page_a import MoovSmartMain

URL = "http://localhost:4200"


class TestUresKerese:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--lang=hu")

        self.browser = webdriver.Chrome(options=options)
        self.browser.get("http://localhost:4200")

    def teardown_method(self):
        self.browser.quit()

    @allure.title("Üres keresés")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Functional", "Read")
    def test_house_found(self):
        home_page = MoovSmartMain(self.browser, URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("Magyar")
        search_page = BasePage(self.browser)

        search_page.search_location("Budapest")

        assert home_page.helymeghatarozo().is_displayed()


    @allure.title("Üres keresés")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Negative", "Functional", "Read")
    def test_empty_search(self):
        home_page = MoovSmartMain(self.browser, URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("Magyar")
        search_page = BasePage(self.browser)

        search_page.search_location("Székesfehérvár, Budai út, 40. 8000, Hungary")

        assert home_page.helymeghatarozok_szama() == 0, \
            "Megjelent marker, pedig nem kellene."
        # ellemőrizzük, a megadott településen, ahol nincs eladó/kiadó ingatlan, hogy a térképen nincs marker

        assert home_page.nincs_talalat_uzenet(), \
            "Nem jelent meg a 'nincs megjelenítendő ingatlan' üzenet."
        # ellemőrizzük, a megadott településen, ahol nincs eladó/kiadó ingatlan, hogy megjelenik-e az üzenet, hogy "nincs megjelenítendő ingatlan"
