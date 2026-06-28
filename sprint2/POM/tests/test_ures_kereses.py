import allure

from sprint2.POM.page_models.base_page_a import BasePage
from sprint2.POM.page_models.main_page_a import MoovSmartMain
from sprint2.POM.create_driver import get_configured_chrome_driver
from sprint2.POM.testdata.testurls import BASE_URL


class TestUresKerese:

    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page_a = MoovSmartMain(self.browser, BASE_URL)
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.base_page_a = BasePage(self.browser)
        self.main_page.open_webpage()
        self.base_page_a.wait_for_app_ready()

    def teardown_method(self):
        self.browser.quit()

    @allure.title("Üres keresés")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Positive", "Functional", "Read")
    def test_house_found(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("Magyar")
        search_page = BasePage(self.browser)

        search_page.search_location("Budapest")

        assert home_page.helymeghatarozo().is_displayed()


    @allure.title("Üres keresés")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Negative", "Functional", "Read")
    def test_empty_search(self):
        home_page = MoovSmartMain(self.browser, BASE_URL)  # meghívjuk egy másik fájlból az ott definiált változókat
        home_page.select_language("Magyar")
        search_page = BasePage(self.browser)

        search_page.search_location("Székesfehérvár, Budai út, 40. 8000, Hungary")

        assert home_page.helymeghatarozok_szama() == 0, \
            "Megjelent marker, pedig nem kellene."
        # ellemőrizzük, a megadott településen, ahol nincs eladó/kiadó ingatlan, hogy a térképen nincs marker

        assert home_page.nincs_talalat_uzenet(), \
            "Nem jelent meg a 'nincs megjelenítendő ingatlan' üzenet."
        # ellemőrizzük, a megadott településen, ahol nincs eladó/kiadó ingatlan, hogy megjelenik-e az üzenet, hogy "nincs megjelenítendő ingatlan"
