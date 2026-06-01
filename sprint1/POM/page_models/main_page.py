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

    def registration_hu(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Regisztráció']")))

    def login_hu(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Bejelentkezés']")))

    def select_language_en(self):
        select_element =  self.wait.until(EC.element_to_be_clickable((By.XPATH, '//select')))
        select = Select(select_element)
        select.select_by_value("en")

    def registration_en(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Registration']")))

    def login_en(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign In']")))