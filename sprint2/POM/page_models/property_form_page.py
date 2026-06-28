import time

from sprint2.POM.page_models.login_page import LoginPage
from sprint2.POM.page_models.logged_in_page import LoggedIn
from sprint2.POM.page_models.my_properties_page import MyProperties
from sprint2.POM.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PropertyEditPage(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.login_page = LoginPage(self.browser, URL)
        self.logged_in_page = LoggedIn(self.browser, URL)
        self.my_properties_page = MyProperties(self.browser, URL)
        self.wait = WebDriverWait(self.browser, 5)

    def button_facts(self) -> WebElement:
        """Kinyitja a Facts szekciót - Automatikus odagördüléssel."""
        element = self.wait.until(EC.element_to_be_clickable((By.ID, "button1")))
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        return element

    def button_location(self) -> WebElement:
        """Kinyitja a Location szekciót - Automatikus odagördüléssel."""
        element = self.wait.until(EC.element_to_be_clickable((By.ID, "button2")))
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        return element

    def button_features(self) -> WebElement:
        """Kinyitja a Features szekciót - Automatikus odagördüléssel."""
        element = self.wait.until(EC.element_to_be_clickable((By.ID, "button3")))
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        return element

    def input_sell(self) -> WebElement:
        """A 'SELL' radio button az id alapján - JavaScriptes kattintás-támogatással."""
        element = self.wait.until(EC.presence_of_element_located((By.ID, "SELL")))

        def js_click():
            self.browser.execute_script("arguments[0].click();", element)

        element.click = js_click
        return element

    def input_rent(self) -> WebElement:
        """A 'RENT' radio button az id alapján - JavaScriptes kattintás-támogatással."""
        element = self.wait.until(EC.presence_of_element_located((By.ID, "RENT")))

        def js_click():
            self.browser.execute_script("arguments[0].click();", element)

        element.click = js_click
        return element

    def input_price(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, "price")))

    def input_square_meter(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, "squareMeter")))

    def input_year_built(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "yearBuilt")))

    def input_number_of_rooms(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, "numberOfRooms")))

    def input_number_of_baths(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "numberOfBaths")))

    def input_address(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.geoapify-autocomplete-input")))

    def autocomplete_first_result_address(self) -> WebElement:
        """A legelső felajánlott cím-találat az autocomplete listában."""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.geoapify-autocomplete-item")))

    def textarea_description(self) -> WebElement:
        # Javítva a stabil EC verzióra!
        return self.wait.until(EC.element_to_be_clickable((By.ID, "description")))

    def button_save_property(self) -> WebElement:
        """A form alján található 'Save Property' megerősítő gomb - Beépített JS-kattintással."""
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-primary.my-buttons")))

        def js_click():
            self.browser.execute_script("arguments[0].click();", element)

        element.click = js_click
        return element

    def _execute_login_my_properties(self, email, password, property_address):
        # 1. Bejelentkezés elvégzése
        self.login_page._execute_login(email, password)
        print("[Property Form Page] Login adatok elküldve.")

        # 2. Megvárjuk, amíg a V2-es My Profile gomb stabilan megjelenik és rákattintunk
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.navbar-side-items-link.my-profile"))
        ).click()
        print("[Property Form Page] A My Profile gomb megjelent, indítjuk a navigációt...")

        # 3. Biztonságos navigáció a V2-es lenyíló menün keresztül
        self.logged_in_page.navigate_to_my_properties()

        # 4. Kattintás az adott ingatlan EDIT gombjára
        self.my_properties_page.click_edit_on_property(property_address)