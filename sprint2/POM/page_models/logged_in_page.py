import time

from sprint2.POM.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoggedIn(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 5)

        # V2-es Hamburger/Menu gomb lokátor (az img ID-ja alapján a legbiztosabb)
        self.hamburger_button = (By.CSS_SELECTOR, "#button-menu")

        # V2-es univerzális profil navigációs lokátorok (mobil és asztali nézetben is megegyeznek!)
        self.button_my_profile_locator = (By.CSS_SELECTOR, "a.navbar-side-items-link.my-profile")
        self.button_my_properties_locator = (By.CSS_SELECTOR, "a.profile-link[routerlink='/my-property-list']")

    def button_exit(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Logout') or contains(text(), 'Kijelentkezés')]")))

    def navigate_to_my_properties(self):
        time.sleep(1)

        # 1. LÉPÉS: Ha kis képernyőn vagyunk, először megnyitjuk a hamburger menüt
        hamburger_elements = self.browser.find_elements(*self.hamburger_button)

        if len(hamburger_elements) > 0 and hamburger_elements[0].is_displayed():
            print("[Logged In] Kis képernyő észlelve, hamburger menü megnyitása...")
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(self.hamburger_button)
            ).click()
            time.sleep(0.5)  # Beúszó animáció megvárása

        # 2. LÉPÉS: Innentől a logika közös (asztali és mobil nézetben is)!
        print("[Logged In] Kattintás a My Profile menüre...")
        my_profile_btn = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.button_my_profile_locator)
        )
        my_profile_btn.click()

        print("[Logged In] My Profile lenyitva, kattintás a My Properties opcióra...")

        # Megvárjuk, amíg a 'visually-hidden' eltűnik és a link ténylegesen láthatóvá/kattinthatóvá válik
        my_properties_sub_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.button_my_properties_locator)
        )
        self.browser.execute_script("arguments[0].click();", my_properties_sub_btn)

        time.sleep(1)