from sprint1.POM.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class MoovSmartMain(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 5)

    def select_language_hu(self):
        select_element =  self.wait.until(EC.element_to_be_clickable((By.XPATH, '//select')))
        select = Select(select_element)
        select.select_by_value("hu")

    def select_language_en(self):
        select_element =  self.wait.until(EC.element_to_be_clickable((By.XPATH, '//select')))
        select = Select(select_element)
        select.select_by_value("en")

    def registration(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='my-navbar-right-links']/a)[2]")))

    def login(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign In')]")))

    def logo_prohouse(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='brand']")))

    def for_buy_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='navlink hover-underline-animation'])[1]")))

    def for_rent_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='navlink hover-underline-animation'])[2]")))

    def search_bar(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='geoapify-autocomplete-input']")))

    def search_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn header-search-button']")))

    def recent_sale_back_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sale-slide-back']")))

    def recent_sale_forward_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sale-slide']")))

    def recent_property_for_sale_1(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[1]")))

    def recent_property_for_sale_2(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[2]")))

    def recent_property_for_sale_3(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[3]")))

    def recent_property_for_sale_4(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[4]")))

    def recent_rent_back_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='rent-slide-back']")))

    def recent_rent_forward_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='rent-slide']")))

    def recent_property_for_rent_1(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[5]")))

    def recent_property_for_rent_2(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[6]")))

    def recent_property_for_rent_3(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[7]")))

    def recent_property_for_rent_4(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/img[@class='main-list-item-image'])[8]")))



