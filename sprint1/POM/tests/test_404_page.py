import allure


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from sprint1.POM.page_models.error_page_a import ErrorPage
from sprint1.POM.page_models.main_page_a import MoovSmartMain


class TestErrorPage:  # ez a teszt
    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--lang=hu")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get("http://localhost:4200")
        self.main_page_a = MoovSmartMain(self.browser, "http://localhost:4200")
        self.error_page = ErrorPage(self.browser)

    def teardown_method(self):
        self.browser.quit()

    @allure.title("404-es oldal megjelenítése")
    @allure.description("Error page")
    @allure.severity(allure.severity_level.CRITICAL)
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
