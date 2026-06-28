import allure

from sprint2.POM.page_models.base_page_a import BasePage
from sprint2.POM.page_models.error_page_a import ErrorPage
from sprint2.POM.page_models.main_page_a import MoovSmartMain
from sprint2.POM.create_driver import get_configured_chrome_driver
from sprint2.POM.testdata.testurls import BASE_URL


class TestErrorPage:  # ez a teszt
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page_a = MoovSmartMain(self.browser, BASE_URL)
        self.error_page = ErrorPage(self.browser)
        self.base_page_a = BasePage(self.browser)
        self.main_page_a.open_webpage()
        self.base_page_a.wait_for_app_ready()

    def teardown_method(self):
        self.browser.quit()

    @allure.title("404-es oldal megjelenítése")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Negative", "Read")
    def test_404_page(self):
        self.main_page_a.search_for_address("Székesfehérvár")

        is_displayed = self.error_page.is_404_displayed()

        if not is_displayed:
            print("\n[BUG] A 404-es oldal nem jelent meg nem létező ingatlan keresése után.")
            print("[BUG] Elvárt: 404-es hibaoldal megjelenítése.")
            print("[BUG] Tényleges: Az oldal nem ad visszajelzést a felhasználónak.")

        assert is_displayed, (
            "BUG: Nem létező ingatlan keresése esetén az alkalmazás nem jelenít meg "
            "404-es hibaoldalt. Az oldal hibásan működik.")
