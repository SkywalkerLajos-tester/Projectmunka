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

        # A megerősítő ablakban lévő törlés gomb (vagy gombok)
        self.confirm_delete_panel = (By.CSS_SELECTOR, "div.confirm-delete")
        self.confirm_delete_button = (By.XPATH, "//div[contains(@class, 'confirm-delete')]//button")

    # --- 2. DINAMIKUS LOKÁTOR GENERÁTOROK ---
    # Mivel a gombot a címe alapján kell megtalálnunk, a lokátort egy külön függvény generálja le
    def _get_delete_button_locator_by_title(self, property_address):
        """Létrehozza a specifikus törlés gomb lokátorát az ingatlan címe alapján."""
        xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'btn-delete')]"
        return (By.XPATH, xpath)

    # --- 3. ELEM ELÉRÉSI METÓDUSOK (GETTEREK) ---
    def get_delete_button(self, property_address):
        """Megvárja, odagördül és visszaadja a törlendő ingatlan törlés gombját."""
        locator = self._get_delete_button_locator_by_title(property_address)

        # 1. Megvárjuk, amíg az elem egyáltalán jelen van a HTML-ben (DOM)
        button_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )

        print(f"[POM] Ingatlan megtalálva a kódban, odagördülés a(z) {property_address}. találathoz...")

        # 2. GOLYÓÁLLÓ GÖRGETÉS: JavaScript segítségével pontosan a gombhoz görgetjük a képernyőt.
        # A {'block': 'center'} biztosítja, hogy a gomb a képernyő KÖZEPÉRE kerüljön,
        # így a fix fejléc (header) biztosan nem fogja kitakarni!
        self.browser.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button_element
        )

        # Várunk egy pici tizedmásodpercet, amíg a sima (smooth) görgetési animáció lezajlik
        time.sleep(0.5)

        # 3. Most már biztosan látható és kattintható, visszaadjuk a gombot
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )

    def get_confirm_button(self):
        """Megvárja és visszaadja a felugró panel megerősítő gombját."""
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.confirm_delete_button)
        )

    # --- 4. AKCIÓ METÓDUSOK (MŰVELETEK) ---
    def click_delete_on_property(self, property_address):
        """Első lépés: rákattint az ingatlan saját Delete gombjára."""
        print(f"[POM] Kattintás a(z) '{property_address}' ingatlan Delete gombjára.")
        self.get_delete_button(property_address).click()

    def click_confirm_delete(self, property_address: str) -> WebElement:
        # 1. Megkeressük a kártyát, ami tartalmazza a címet
        # 2. Azon belül megkeressük a confirm-delete-yes gombot
        exact_xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'confirm-delete-yes')]"

        button_yes = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, exact_xpath))
        )
        button_yes.click()

    def click_cancel_delete(self, property_address: str) -> None:
        """Rákattint a felugró ablak CANCEL gombjára az ingatlan címe alapján."""
        print(f"[POM] Törlés megszakítása: Kattintás a 'CANCEL' gombra a(z) '{property_address}' ingatlannál.")
        # A korábbi képernyőképed alapján a Cancel gomb osztálya: 'confirm-delete-cancel'
        exact_xpath = f"//div[contains(@class, 'main-list-item')][descendant::*[contains(text(), '{property_address}')]]//button[contains(@class, 'confirm-delete-cancel')]"

        button_cancel = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, exact_xpath))
        )
        button_cancel.click()
