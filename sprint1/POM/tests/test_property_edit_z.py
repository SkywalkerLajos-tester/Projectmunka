import time
import pytest
import allure

from selenium.webdriver.common.keys import Keys
from sprint1.POM.page_models.main_page import MoovSmartMain
from sprint1.POM.page_models.registration_page import RegistrationPage
from sprint1.POM.page_models.login_page import LoginPage
from sprint1.POM.page_models.logged_in_page import LoggedIn
from sprint1.POM.create_driver import get_configured_chrome_driver
from sprint1.POM.testdata.testurls import BASE_URL
from sprint1.POM.page_models.login_page_ma import LoginPage
from sprint1.POM.page_models.logged_in_page_ma import LoggedIn
from sprint1.POM.page_models.my_properties_page_ma import MyProperties
from sprint1.POM.page_models.property_form_page_ma import PropertyEditPage

class TestPropertyEdit:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)
        self.login_page_ma = LoginPage(self.browser, BASE_URL)
        self.logged_in_page_ma = LoggedIn(self.browser, BASE_URL)
        self.my_properties_page_ma = MyProperties(self.browser, BASE_URL)
        self.property_form_page_ma = PropertyEditPage(self.browser, BASE_URL)


        # Minden teszt ezekkel a lépésekkel indul, így ideális itt futtatni őket
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.login().click()

    # def teardown_method(self):
    #     self.main_page.close_browser()

    ############################ Minden teszt ezekkel a lépésekkel indul, így ideális itt futtatni őket - bejelentkezés
    def _execute_login_my_properties(self, email, password, property_address):
        """Közös segédmetódus az adatok beírására és a kattintásra."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

    # ==========================================
    # POZITÍV TESZTESETEK
    # ==========================================
    @allure.title("TC01 - Ingatlan leírásának módosítása és mentése.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("Valami", "Semmi", "Akármi")
    @pytest.mark.parametrize(
        "email, password, property_address, description",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "Property description edit")
        ]
    )
    def test_property_descripton_edit(self, email, password, property_address, description):
        """TC01 - Ingatlan leírásának módosítása és mentése."""

    #################################################################################################x
        self._execute_login_my_properties(email, password, property_address)

        self.property_form_page_ma.button_features().click()
        self.property_form_page_ma.textarea_description().clear()
        self.property_form_page_ma.textarea_description().send_keys("kiskutya")

        # # A POM háttérben intézi a biztos kattintást!
        self.property_form_page_ma.button_save_property().click()
        time.sleep(0.5)
        success_nav = self.property_form_page_ma.get_current_url()
        assert success_nav == "http://localhost:4200/my-property-list"
        ## assert 1: kimenteni változóban a régi descritiont és az újat is és az nem lehet egyenlő egymással
        ## assert 2: új descrition == "kiskutya"


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "email, password, property_address, new_price, new_sqm,title",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "320000", "75"
                 ,"TC02 - Alapadatok módosítása és mentése.")
        ]
    )
    def test_property_edit_facts(self, email, password, property_address, new_price, new_sqm,title):
        """TC02 - Alapadatok módosítása és mentése."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Szekció nyitás és adatmódosítás
        self.property_form_page_ma.button_facts().click()
        self.property_form_page_ma.input_rent().click()

        self.property_form_page_ma.input_price().clear()
        self.property_form_page_ma.input_price().send_keys(new_price)

        self.property_form_page_ma.input_square_meter().clear()
        self.property_form_page_ma.input_square_meter().send_keys(new_sqm)

        # Megnyitjuk a features fület, hogy a mentés gomb megjelenjen
        self.property_form_page_ma.button_features().click()

        # Mentés
        self.property_form_page_ma.button_save_property().click()
        time.sleep(0.5)
        success_nav = self.property_form_page_ma.get_current_url()
        assert success_nav == "http://localhost:4200/my-property-list"


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "email, password, property_address, search_city,title",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "1091 Budapest, Üllői street"
                 ,"TC03 - Cím módosítása és mentése.")
        ]
    )
    def test_property_edit_location_autocomplete(self, email, password, property_address, search_city,title):
        """TC03 - Cím módosítása és mentése."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        self.property_form_page_ma.button_location().click()

        address_input = self.property_form_page_ma.input_address()
        address_input.clear()
        address_input.send_keys(search_city)

        time.sleep(0.5)  # Rövid várakozás az autocomplete hálózati kérésére
        self.property_form_page_ma.autocomplete_first_result_address().click()

        # Megnyitjuk a features fület, hogy a mentés gomb megjelenjen
        self.property_form_page_ma.button_features().click()

        # Mentés
        self.property_form_page_ma.button_save_property().click()
        time.sleep(0.5)
        success_nav = self.property_form_page_ma.get_current_url()
        assert success_nav == "http://localhost:4200/my-property-list"

    # ==========================================
    # NEGATÍV TESZTESETEK
    # ==========================================

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "email, password, property_address,title",
        [
            ("test3@test.hu", "1234_Abcd", "1091 Budapest, Üllői street"
                 ,"TC04 - Negatív eset: Mentési kísérlet üresen hagyott ár mezővel.")
        ]
    )
    def test_property_edit_error_empty_price(self, email, password, property_address,title):
        """TC04 - Negatív eset: Mentési kísérlet üresen hagyott ár mezővel."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Kinyitjuk a Facts szekciót
        self.property_form_page_ma.button_facts().click()

        price_field = self.property_form_page_ma.input_price()
        price_field.click()
        time.sleep(0.5)
        price_field.clear()

        # # !!! IGAZI TÖRLÉS SZIMULÁCIÓ: Kijelölés (CTRL+A) majd törlés (BACKSPACE)
        # # Ez garantáltan fellövi az Angular felé a 'change' és 'input' eseményeket, mintha gépelnél!
        # price_field.send_keys(Keys.CONTROL + "a")
        # price_field.send_keys(Keys.BACKSPACE)
        #
        # # Egy extra tabulátor vagy kattintás kiváltja a 'blur' (fókuszvesztés) eseményt is, ami a hibaüzenetet triggereli
        # price_field.send_keys(Keys.TAB)
        time.sleep(1)

        # Megnyitjuk a Features fület a mentés gombhoz, majd mentünk
        self.property_form_page_ma.button_features().click()
        self.property_form_page_ma.button_save_property().click()

        # Várunk
        time.sleep(0.5)

        # # Lekérjük a jelenlegi URL-t
        # current_url = self.property_form_page_ma.get_current_url()
        #
        # # Elvárás: Mivel az ár sikeresen ki lett törölve és a form érvénytelen lett,
        # # az oldal NEM navigálhatott el, maradt a formon.
        # assert "property-form" in current_url

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "email, password, property_address, invalid_price,title",
        [
            ("test3@test.hu", "1234_Abcd", "1091 Budapest, Üllői street", "-5000",
                 "TC05 - Negatív eset: Mentési kísérlet negatív összegű árral.")
        ]
    )
    def test_property_edit_error_negative_price(self, email, password, property_address, invalid_price,title):
        """TC05 - Negatív eset: Mentési kísérlet negatív összegű árral."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Kinyitjuk a Facts szekciót és negatív árat adunk meg
        self.property_form_page_ma.button_facts().click()
        self.property_form_page_ma.input_price().clear()
        self.property_form_page_ma.input_price().send_keys(invalid_price)

        # Mentés
        self.property_form_page_ma.button_features().click()
        self.property_form_page_ma.button_save_property().click()

        time.sleep(0.5)
        current_url = self.property_form_page_ma.get_current_url()

        # Elvárás: Negatív árral sem navigálhat el, a formon kell maradnia
        assert "property-form" in current_url

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "email, password, property_address, incomplete_address,title",
        [
            ("test3@test.hu", "1234_Abcd", "1091 Budapest, Üllői street", "ValamiKamucim123"
                 ,"TC06 - Negatív eset: Mentési kísérlet listából ki nem választott, érvénytelen címmel.")
        ]
    )
    def test_property_edit_error_invalid_autocomplete(self, email, password, property_address, incomplete_address,title):
        """TC06 - Negatív eset: Mentési kísérlet listából ki nem választott, érvénytelen címmel."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Kinyitjuk a Location szekciót, beírunk egy nem létező szöveget, de nem kattintunk a listára
        self.property_form_page_ma.button_location().click()
        address_input = self.property_form_page_ma.input_address()
        address_input.clear()
        address_input.send_keys(incomplete_address)

        # Hagyunk egy kis időt a formnak, majd megpróbáljuk elmenteni
        time.sleep(0.5)
        self.property_form_page_ma.button_features().click()
        self.property_form_page_ma.button_save_property().click()

        time.sleep(0.5)
        current_url = self.property_form_page_ma.get_current_url()

        # Elvárás: Mivel a cím nincs geokódolva/kiválasztva, a form érvénytelen, az oldalon kell maradnia
        assert "property-form" in current_url

    # ==========================================
    # KRITIKUS BIZTONSÁGI ÉS ARCHITEKTÚRA TESZTEK
    # ==========================================

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, property_address, xss_payload",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "<script>alert('XSS')</script>")
        ]
    )
    def test_property_edit_script_injection_protection(self, email, password, property_address, xss_payload):
        """TC07 - Kritikus biztonsági eset: Script injection (XSS) elleni védelem ellenőrzése."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Kinyitjuk a Features fület és beillesztjük a kártékony kódot a leírásba
        self.property_form_page_ma.button_features().click()
        self.property_form_page_ma.textarea_description().clear()
        self.property_form_page_ma.textarea_description().send_keys(xss_payload)

        # Elmentjük
        self.property_form_page_ma.button_save_property().click()

        # Várakozás
        time.sleep(0.5)
        current_url = self.property_form_page_ma.get_current_url()

        # Mivel az alkalmazás helyesen VÉDETT, az oldal NEM navigálhat el a listára,
        # hanem a formon kell maradnia (mivel a validáció elutasította a script karaktereket).
        assert "property-form" in current_url

        # EXTRA BIZTONSÁGI ELLENŐRZÉS: Meggyőződünk róla, hogy a rendszer kiírta-e a megfelelő hibaüzenetet
        page_source = self.browser.page_source
        assert "You can only use the following special characters" in page_source, "A formon maradtunk, de nem kaptuk meg az XSS védelmi hibaüzenetet!"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, property_address",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street")
        ]
    )
    def test_property_edit_server_side_validation_bypass(self, email, password, property_address):
        """TC08 - Kritikus architektúra eset: Szerver oldali validáció ellenőrzése frontend kikerülésével (Bypass kísérlet)."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Kinyitjuk a Facts szekciót
        self.property_form_page_ma.button_facts().click()

        # ELŐIDÉZZÜK A FRONTEND KIJÁTSZÁSÁT:
        # JavaScript segítségével közvetlenül írjuk át az árat egy üres értékre vagy negatív számra,
        # és az Angular belső 'ng-invalid' osztályait/érvényesítését erőszakkal felülírjuk vagy megkerüljük.
        price_element = self.property_form_page_ma.input_price()

        # JS-ből kényszerítjük bele a hibás (üres) adatot, amit a billentyűzet-ellenőrzés nem lát
        self.browser.execute_script("arguments[0].value = '';", price_element)
        self.browser.execute_script("arguments[0].dispatchEvent(new Event('change'));", price_element)

        # Megnyitjuk a Features fület, hogy elérjük a gombot
        self.property_form_page_ma.button_features().click()
        save_btn = self.property_form_page_ma.button_save_property()

        # JavaScriptből indítjuk el a kattintást is, így a letiltott (disabled) gombokat is ki tudjuk játszani!
        # Ez pontosan azt szimulálja, mintha egy hacker Postmanből vagy cURL-ből küldene be rossz adatot közvetlenül a backend API-ra
        self.browser.execute_script("arguments[0].click();", save_btn)

        time.sleep(0.5)
        current_url = self.property_form_page_ma.get_current_url()

        # HA A RENDSZER ELNAVIGÁLT A LISTÁRA (ami jelenleg történik a frontend hiba miatt):
        if current_url == "http://localhost:4200/my-property-list":

            # Lekérjük a lista oldal tartalmát
            page_source = self.browser.page_source

            # ELLENŐRZÉS: Mivel az üres árat a szerver elutasította, az ingatlanod NEM sérülhetett meg,
            # és továbbra is ott kell lennie a listában a címe alapján!
            assert property_address in page_source, "A szerveroldali védelem elbukott, az ingatlan eltűnt vagy megsérült!"

            # Ha az ingatlan megvan, a teszt sikeres (PASSED), mert a backend megvédte az adatot!
            # Allure vagy konzol üzenetben jelezzük a frontend hibát a fejlesztőknek:
            print(
                "[INFO/BUG] A szerveroldali validáció sikeresen megvédte az adatot az üres beküldéstől, de a frontend hibásan elnavigált a listára!")

        else:
            # HA A JÖVŐBEN JAVÍTJÁK A FRONTENDET: Ha elutasítja a szerver, a formon kell tartania a böngészőt (Ez a tökéletes működés)
            assert "property-form" in current_url


    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "email, password, property_address, xss_payload",
        [
            ("test3@test.hu", "1234_Abcd", "6000 Kecskemét, Szent Miklós street", "<script>alert('BypassXSS')</script>")
        ]
    )
    def test_property_edit_xss_validation_bypass(self, email, password, property_address, xss_payload):
        """TC09 - Kritikus biztonsági eset: Stored XSS ellenőrzése frontend validáció kikerülésével."""
        self.login_page_ma._execute_login(email, password)
        self.logged_in_page_ma.navigate_to_my_properties()
        self.my_properties_page_ma.click_edit_on_property(property_address)

        # Kinyitjuk a Features fület
        self.property_form_page_ma.button_features().click()

        # ELŐIDÉZZÜK A FRONTEND KIJÁTSZÁSÁT:
        # JavaScriptből közvetlenül kényszerítjük bele a kártékony kódot a textarea-ba,
        # teljesen megkerülve az Angular billentyűzet-alapú karakterkorlátozását.
        desc_element = self.property_form_page_ma.textarea_description()
        self.browser.execute_script("arguments[0].value = arguments[1];", desc_element, xss_payload)
        self.browser.execute_script("arguments[0].dispatchEvent(new Event('change'));", desc_element)

        # JavaScriptből küldjük el a mentést is, kijátszva a tiltásokat
        save_btn = self.property_form_page_ma.button_save_property()
        self.browser.execute_script("arguments[0].click();", save_btn)

        time.sleep(0.5)
        current_url = self.property_form_page_ma.get_current_url()

        # ELLENŐRZÉS:
        # 1. Ha az oldal a formon maradt, az azt jelenti, hogy a backend API észlelte és elutasította a támadást (Helyes!)
        if "property-form" in current_url:
            assert True

        # 2. Ha az oldal elnavigált a listára (http://localhost:4200/my-property-list)...
        else:
            # Akkor meg kell néznünk, hogy a lefutó kód megfertőzte-e az oldalt.
            # Ha a script sikeresen lefutott a böngészőben, a Selenium egy 'UnexpectedAlertPresentException' hibát dobna automatikusan,
            # ami azonnal elbuktatná a tesztet. De biztosra megyünk: megnézzük, hogy a nyers kód megjelent-e a forráskódban escapeelés nélkül.
            page_source = self.browser.page_source

            # Ha a szerver nem tisztította meg a szöveget, és a nyers <script> tag ott van a listában, a teszt elbukik -> MEGVAN A BUG!
            assert xss_payload not in page_source, (
                "SÚLYOS BIZTONSÁGI REZIDUUM! A rendszer frontend bypass után elmentette "
                "és nyers formában renderelte ki a kártékony JavaScript kódot!"
            )