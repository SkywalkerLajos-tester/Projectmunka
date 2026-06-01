from sprint1.POM_registration.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class RegistrationPage(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 5)

    def last_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "lastName")))

    def first_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "firstName")))

    def phone_number(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "phoneNumber")))

    def email(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "email")))

    def confirm_email(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "confirmEmail")))

    def password(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "password")))

    def confirm_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "confirmPassword")))

    def button_registration(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn'])[2]")))

