import pytest
import allure
import json
import time
import mysql.connector

from sprint2.POM.page_models.main_page import MoovSmartMain
from sprint2.POM.page_models.registration_page import RegistrationPage
from sprint2.POM.page_models.login_page import LoginPage
from sprint2.POM.page_models.logged_in_page import LoggedIn
from sprint2.POM.create_driver import get_configured_chrome_driver
from sprint2.POM.testdata.testuser_reg import TESTUSER
from sprint2.POM.testdata.testurls import BASE_URL


class TestRegistration:
    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.main_page = MoovSmartMain(self.browser, BASE_URL)
        self.registration_page = RegistrationPage(self.browser, BASE_URL)
        self.login_page = LoginPage(self.browser, BASE_URL)
        self.logged_in_page = LoggedIn(self.browser, BASE_URL)

        # Minden teszt ezzel kezdődik
        self.main_page.open_webpage()
        self.main_page.select_language_en()
        self.main_page.registration().click()

    # def teardown_method(self):
    #     self.main_page.close_browser()

    def is_user_registered_in_db(self, email):
        """Lekérdezi a Dockerben futó MySQL adatbázist, hogy létezik-e az email."""
        try:
            # Kapcsolódás a localhalthoz, mivel a Docker kiengedi a 3306-os portot
            connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",  # Írd át, ha más a user a docker-compose-ban
                password="test1234",  # Írd át a docker-ben megadott jelszóra
                database="moovsmart"  # Írd át a pontos adatbázis nevére
            )
            cursor = connection.cursor()

            # SQL lekérdezés (írd át a tábla és oszlopneveket, ha szükséges)
            query = "SELECT COUNT(*) FROM users WHERE email = %s"
            cursor.execute(query, (email,))

            (count,) = cursor.fetchone()

            cursor.close()
            connection.close()

            return count > 0

        except mysql.connector.Error as err:
            pytest.fail(f"Adatbázis kapcsolódási hiba: {err}")


    def fill_registration_form_and_submit(self, user_data, click_submit=True):
        """Helper metódus az űrlap kitöltéséhez és a beküldéshez."""
        allure.attach(json.dumps(user_data, indent=4, ensure_ascii=False),
            name="Felhasznált tesztadatok (TESTUSER)",
            attachment_type=allure.attachment_type.JSON)

        reg = self.registration_page

        reg.last_name().send_keys(user_data["lastname"])
        reg.first_name().send_keys(user_data["firstname"])
        reg.phone_number().send_keys(user_data["phone_number"])
        reg.email().send_keys(user_data["email"])
        reg.confirm_email().send_keys(user_data["email_confirm"])
        reg.password().send_keys(user_data["password"])
        reg.confirm_password().send_keys(user_data["password_confirm"])

        if click_submit:
            button = reg.button_registration()
            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(0.5)
            button.click()
            time.sleep(0.5)

# -------------------------------------------------------------------------
# TESZTESETEK
# -------------------------------------------------------------------------

    @allure.title("Registration eng tc01")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration - valid", ["Valid registration"])
        ]
    )
    def test_registration_eng_valid(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[0])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[0]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is True, f"Hiba! A regisztráció sikertelen: a(z) '{target_email}' email cím nem található meg az adatbázisban!"

    @allure.title("Registration eng tc02")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with same email", ["Registration - same email"])
        ]
    )
    def test_registration_eng_with_same_email(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        self.fill_registration_form_and_submit(TESTUSER[0])

        error_msg = self.registration_page.error_email_missing_or_wrong_single()
        assert error_msg.is_displayed()
        assert error_msg.text == "Email address is already taken!"


    @allure.title("Registration eng tc03")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration without last name", ["Registration - last name empty"])
        ]
    )
    def test_registration_eng_without_lastname(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[1])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[1]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

        error_msg = self.registration_page.error_last_name()
        assert error_msg.is_displayed()
        assert error_msg.text == "Please enter your last name"


    @allure.title("Registration eng tc04")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration without first name", ["Registration - first name empty"])
        ]
    )
    def test_registration_eng_without_firstname(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[2])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[2]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

        error_msg = self.registration_page.error_first_name()
        assert error_msg.is_displayed()
        assert error_msg.text == "Please enter your first name"


    @allure.title("Registration eng tc05")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration without phone number",
             ["Registration - phone number empty", "Phone number - Not required", "Can be empty"])
        ]
    )
    def test_registration_eng_without_phone_number(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[3])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[3]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is True, f"Hiba! A regisztráció sikertelen: a(z) '{target_email}' email cím nem található meg az adatbázisban!"

        assert not self.registration_page.error_phone_number().is_displayed()


    @allure.title("Registration eng tc06")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with invalid names and phone number",
             ["Registration - numbers in names", "Registration - letters in phone number"])
        ]
    )
    def test_registration_eng_with_invalid_names_and_phone(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[4])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[4]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

    @allure.title("Registration eng tc07")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with invalid email", ["Registration - invalid email"])
        ]
    )
    def test_registration_eng_with_invalid_email(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[5])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[5]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

        error_msg = self.registration_page.error_email_missing_or_wrong_single()
        assert error_msg.is_displayed()
        assert error_msg.text == "Not a proper email format!"


    @allure.title("Registration eng tc08")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with wrong email confirmation", ["Registration - wrong email confirmation", "typo"])
        ]
    )
    def test_registration_eng_with_wrong_email_confirm(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Kitöltjük az űrlapot, de még nem küldjük be
        self.fill_registration_form_and_submit(TESTUSER[6], click_submit=False)
        time.sleep(1)

        # 2. Ellenőrizzük, hogy a felületen megjelent-e a hibaüzenet (kliensoldali validáció)
        error_msg = self.registration_page.error_confirm_email()
        assert error_msg.is_displayed()
        assert error_msg.text == "Email does not match"

        # 3. RÁKATTINTUNK a gombra (megpróbáljuk "rosszul" is beküldeni)
        button = self.registration_page.button_registration()
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        button.click()

        # 4. VÁRUNK, hogy a backendnek legyen ideje feldolgozni (ha mégis átengedné)
        time.sleep(1)

        # 5. MOST ellenőrizzük a Docker adatbázist, a kattintás UTÁN!
        target_email = TESTUSER[6]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 6. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"


    @allure.title("Registration eng tc09")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with wrong password", ["Registration - wrong password"])
        ]
    )
    def test_registration_eng_with_wrong_password(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[7])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[7]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

        error_msg = self.registration_page.error_password()
        assert error_msg.is_displayed()
        assert error_msg.text == "Please enter a password"


    @allure.title("Registration eng tc10")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with wrong password confirmation", ["Registration - wrong password confirmation", "typo"])
        ]
    )
    def test_registration_eng_with_wrong_password_confirm(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[8])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[8]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

        error_msg = self.registration_page.error_confirm_password()
        assert error_msg.is_displayed()
        assert error_msg.text == "Password does not match"


    @allure.title("Registration eng tc11")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with wrong email & password confirmation",
             ["Registration - wrong email & password confirmation", "typo"])
        ]
    )
    def test_registration_eng_with_wrong_email_and_password_confirm(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[9])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[9]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"

        error_msg = self.registration_page.error_confirm_email()
        assert error_msg.is_displayed()
        assert error_msg.text == "Email does not match"

        error_msg = self.registration_page.error_confirm_password()
        assert error_msg.is_displayed()
        assert error_msg.text == "Password does not match"


    @allure.title("Registration eng tc12")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "description, tag",
        [
            ("Registration with short names", ["Registration - short names", "Names too short", "Must be at least 3 characters long"])
        ]
    )
    def test_registration_eng_with_short_names(self, description, tag):
        allure.dynamic.description(description)
        allure.dynamic.tag(*tag)

        # 1. Elküldjük a regisztrációt a felületről
        self.fill_registration_form_and_submit(TESTUSER[10])

        # 2. Várunk egy picit, hogy a backend elmenthesse az adatot (a hálózat/konténer sebességétől függően)
        time.sleep(1)

        # 3. Közvetlen ellenőrzés a Docker adatbázisban
        target_email = TESTUSER[10]["email"]
        is_in_db = self.is_user_registered_in_db(target_email)

        # 4. Az Asszertáció
        assert is_in_db is False, f"Hiba! A regisztráció sikeres: a(z) '{target_email}' email cím megtalálható az adatbázisban!"
