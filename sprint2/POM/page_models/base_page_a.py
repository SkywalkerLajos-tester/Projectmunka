import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.search_input = (By.CSS_SELECTOR, "input.geoapify-autocomplete-input")
        self.suggestion = (By.CSS_SELECTOR, ".geoapify-autocomplete-item")
        self.search_button = (By.XPATH, '//button[@class="btn header-search-button"]')

    def search_location(self, text):
        search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input))
        search.click()
        search.send_keys(text)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.suggestion)).click()

        self.driver.find_element(*self.search_button).click()

    def wait_for_app_ready(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.geoapify-autocomplete-input"))
            )
        except TimeoutException:
            pytest.fail(
                f"Az alkalmazás {timeout} mp alatt nem töltődött be. "
                f"Ellenőrizd, hogy a Docker konténerek futnak-e."
            )