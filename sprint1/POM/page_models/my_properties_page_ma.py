import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class MyProperties:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

        # --- 1. STATIKUS LOKÁTOROK ---
        # Az összes ingatlan kártya közös osztálya
        self.property_cards = (By.CSS_SELECTOR, "div.main-list-item")

    # --- 2. DINAMIKUS LOKÁTOR GENERÁTOROK ---
    def _get_delete_button_locator_by_address(self, property_address):
        """Létrehozza a specifikus törlés gomb lokátorát az ingatlan pontos címe alapján."""
        xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'btn-delete')]"
        return (By.XPATH, xpath)

    def _get_edit_button_locator_by_address(self, property_address):
        """Létrehozza a specifikus szerkesztés (Edit) gomb lokátorát az ingatlan pontos címe alapján."""
        xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'btn-edit')]"
        return (By.XPATH, xpath)

    def _get_upload_button_locator_by_address(self, property_address):
        """Létrehozza a specifikus feltöltés (Upload) gomb lokátorát az ingatlan pontos címe alapján."""
        xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'btn-upload')]"
        return (By.XPATH, xpath)

    # --- 3. ELEM ELÉRÉSI METÓDUSOK (GETTEREK) ---
    def get_delete_button(self, property_address) -> WebElement:
        """Megvárja, odagördül és visszaadja a törlendő ingatlan törlés gombját."""
        locator = self._get_delete_button_locator_by_address(property_address)

        # Megvárjuk, amíg az elem egyáltalán jelen van a HTML-ben (DOM)
        button_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )

        print(f"[POM] Ingatlan megtalálva a kódban, odagördülés a(z) {property_address} találathoz...")

        # GÖRGETÉS
        self.browser.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button_element
        )

        time.sleep(0.5)

        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )

    def get_edit_button(self, property_address) -> WebElement:
        """Megvárja, odagördül és visszaadja a kiválasztott ingatlan Edit gombját."""
        locator = self._get_edit_button_locator_by_address(property_address)

        button_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )

        print(f"[POM] Ingatlan megtalálva a kódban, odagördülés az Edit gombhoz: {property_address}...")

        self.browser.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button_element
        )

        time.sleep(0.5)

        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )

    def get_upload_button(self, property_address) -> WebElement:
        """Megvárja, odagördül és visszaadja a kiválasztott ingatlan Upload gombját."""
        locator = self._get_upload_button_locator_by_address(property_address)

        button_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )

        print(f"[POM] Ingatlan megtalálva a kódban, odagördülés az Upload gombhoz: {property_address}...")

        self.browser.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button_element
        )

        time.sleep(0.5)

        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )

    def get_confirm_yes_button(self, property_address: str) -> WebElement:
        """Megvárja és visszaadja a felugró ablak YES gombját az ingatlan címe alapján."""
        exact_xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'confirm-delete-yes')]"
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, exact_xpath))
        )

    def get_confirm_cancel_button(self, property_address: str) -> WebElement:
        """Megvárja és visszaadja a felugró ablak CANCEL gombját az ingatlan címe alapján."""
        exact_xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'confirm-delete-cancel')]"
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, exact_xpath))
        )

    # --- 4. AKCIÓ METÓDUSOK (MŰVELETEK) ---
    def click_delete_on_property(self, property_address: str) -> None:
        """Első lépés: rákattint az ingatlan saját Delete gombjára."""
        print(f"[POM] Kattintás a(z) '{property_address}' ingatlan Delete gombjára.")
        self.get_delete_button(property_address).click()

    def click_edit_on_property(self, property_address: str) -> None:
        """Rákattint az ingatlan saját Edit gombjára a címe alapján."""
        print(f"[POM] Kattintás a(z) '{property_address}' ingatlan Edit gombjára.")
        self.get_edit_button(property_address).click()

    def click_upload_on_property(self, property_address: str) -> None:
        """Rákattint az ingatlan saját Upload gombjára."""
        print(f"[POM] Kattintás a(z) '{property_address}' ingatlan Upload gombjára.")
        self.get_upload_button(property_address).click()

    def click_confirm_delete(self, property_address: str) -> None:
        """Törlés megerősítése: Megkeresi, majd rákattint a felugró ablak YES gombjára."""
        print(f"[POM] Törlés megerősítése: Kattintás a 'YES' gombra a(z) '{property_address}' ingatlannál.")
        self.get_confirm_yes_button(property_address).click()

    def click_cancel_delete(self, property_address: str) -> None:
        """Törlés megszakítása: Megkeresi, majd rákattint a felugró ablak CANCEL gombjára."""
        print(f"[POM] Törlés megszakítása: Kattintás a 'CANCEL' gombra a(z) '{property_address}' ingatlannál.")
        self.get_confirm_cancel_button(property_address).click()
