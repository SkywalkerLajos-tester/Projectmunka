from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from sprint1.POM.general_page import GeneralPage


class MoovSmartMain(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 5)

    SEARCH_INPUT = (By.CSS_SELECTOR, "input.geoapify-autocomplete-input")
    SUGGESTION_ITEM = (By.CSS_SELECTOR, ".geoapify-autocomplete-item")

    def rent_button(self):
        return self.browser.find_element(By.XPATH, " (//a[@class='navlink hover-underline-animation'])[2]")

    def sing_in_button(self):
        return self.browser.find_element(By.XPATH, "(//div[@class='my-navbar-right-links']/a)[1]")

    def email(self):
        return self.browser.find_element(By.XPATH, "//label[@for='email']")

    def password(self):
        return self.browser.find_element(By.XPATH, "//label[@for='password']")

    def text_center(self):
        return self.browser.find_element(By.XPATH, ('//div[@class ="text-center"]'))

    def registration_button(self):
        return self.browser.find_element(By.XPATH, "(//div[@class='my-navbar-right-links']/a)[2]")

    def registration_word(self):
        return self.browser.find_element(By.XPATH, ('//h3[@class="main-title"]'))

    def last_name_word(self):
        return self.browser.find_element(By.XPATH, "//label[@for='lastName']")

    def first_name_word(self):
        return self.browser.find_element(By.XPATH, "//label[@for='firstName']")

    def phone_number_word(self):
        return self.browser.find_element(By.XPATH, "//label[@for='phoneNumber']")

    def email_address_word(self):
        return self.browser.find_element(By.XPATH, "//label[@for='email']")

    def email_address_again_word(self):
        return self.browser.find_element(By.XPATH, "//label[@for='confirmEmail']")

    def plaese_enter_a_password_word(self):
        return self.browser.find_element(By.XPATH, "//app-register-form/div/form/div/label[@for='password']")

    def please_enter_a_password_again_word(self):
        return self.browser.find_element(By.XPATH, "//label[@for='confirmPassword']")

    def register_button(self):
        return self.browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Register')]")

    def search_for_address(self, address):
        search = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search.click()
        search.send_keys(address)

        suggestion = self.wait.until(EC.element_to_be_clickable(self.SUGGESTION_ITEM))
        suggestion.click()

        search_button = self.browser.find_element(By.XPATH, '//button[@class="btn header-search-button"]')
        search_button.click()

    def select_language(self, language):
        Select(self.browser.find_element(By.XPATH, "//app-nav/select")).select_by_visible_text(language)

    def get_search_placeholder(self):
        return self.browser.find_element(*self.SEARCH_INPUT).get_attribute("placeholder")

    def get_buy(self):
        return self.browser.find_element(By.XPATH, "(//a[@class='navlink hover-underline-animation'])[1]")

    def header_title(self):
        return self.browser.find_element(By.XPATH, '//div[@class="header-title"]')

    def main_header_title_sale(self):
        return self.browser.find_element(By.XPATH, '//h3[@class="main-header-title" and contains(.,"Recent properties for Sale")]')

    def main_header_title_rent(self):
        return self.browser.find_element(By.XPATH, '//h3[@class="main-header-title" and contains(.,"Recent properties for Rent")]')

    def for_sale_button(self):
        return self.browser.find_element(By.ID, "saleType")

    def city_placeholder(self):
        return self.browser.find_element(By.ID, "city")

    def search_button(self):
        return self.browser.find_element(By.XPATH, '//button[@class="btn main-form-btn"]')

    def helymeghatarozok_szama(self):
        return len(self.browser.find_elements(By.CSS_SELECTOR,"img.leaflet-marker-icon"))

    def helymeghatarozo(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.leaflet-marker-icon")))

    def nincs_talalat_uzenet(self):
        try:
            alert = self.browser.find_element(By.XPATH,"//*[contains(text(),'Nincs találat')]")
            return alert.is_displayed()
            #ha megkapja a "nincs találat" üzenetet akkor igazt (True) ad vissza
        except:
            return False
