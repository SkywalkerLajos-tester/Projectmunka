import time

from sprint1.POM.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class LoggedIn(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 5)
        # A hamburger gomb
        self.hamburger_button = (By.CSS_SELECTOR, "button.my-navbar-button")

        # ÚJ, TŰPONTOS FIZIKAI LOKÁTOR:
        # Azt mondjuk, hogy keresse meg a #side-navbar-t, és azon belül az a[routerlink='/my-property-list'] elemet.
        # Ez kizárja, hogy az asztali menü gombjára akarjon kattintani!
        self.my_properties_mobile_btn = (By.CSS_SELECTOR, "#side-navbar a[routerlink='/my-property-list']")
        # Ez pedig a sima asztali gomb, ha nagy a képernyő
        self.my_properties_desktop_btn = (By.CSS_SELECTOR, "a[routerlink='/my-property-list']")

    def button_exit(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Logout') or contains(text(), 'Kijelentkezés')]")))

    def navigate_to_my_properties(self):
        time.sleep(1)
        hamburger_elements = self.browser.find_elements(*self.hamburger_button)

        if len(hamburger_elements) > 0 and hamburger_elements[0].is_displayed():
            print("[Logged In] Kis képernyő észlelve, hamburger menü megnyitása...")

            # 1. Fizikai kattintás a hamburger menüre
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(self.hamburger_button)
            ).click()

            print("[Logged In] Menü megnyitva, várunk a MOBIL gomb kattinthatóságára...")

            # Adunk egy pici időt a beúszó animációnak, hogy megálljon a gomb, különben mellékattint a Selenium
            time.sleep(0.5)

            # 2. VALÓDI FIZIKAI KATTINTÁS a mobil menüben lévő gombra
            btn = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(self.my_properties_mobile_btn)
            )
            print("[Logged In] Tényleges fizikai kattintás a mobil My Properties gombra.")
            btn.click()

            # Mivel igazi kattintás történt, az Angular érzékeli a navigációt és BE kell csuknia a menüt.
            time.sleep(1)

        else:
            print("[Logged In] Nagy képernyő, sima kattintás a fejlécben.")
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(self.my_properties_desktop_btn)
            ).click()