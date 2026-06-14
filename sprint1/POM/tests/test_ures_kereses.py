import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sprint1.POM.page_models.base_page_a import BasePage
from sprint1.POM.page_models.error_page_a import ErrorPage


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
    @allure.description("Hiányzó térkép")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_empty_search(self):
        search_page = BasePage(self.browser)
        result_page = ErrorPage(self.browser)

        search_page.search_location("Székesfehérvár, Budai út, 40. 8000, Hungary")

        is_map = result_page.check_map_bug()
        # a check_map_bug metódust meghívjuk és az is_map változóba elmenti az eredményt
        assert not is_map, "BUG: map should NOT be visible when no results"
        #ellenőrizzük, hogy a térkép nem látható