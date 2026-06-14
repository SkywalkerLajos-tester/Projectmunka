from sprint1.POM.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 5)

    def email_address(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))

    def enter_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))

    def button_sign_in(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    def wanna_account(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div/a[@href='/registration-form'])[2]")))

    def error_message(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div/small")))

    def sign_in_window(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']")))

    def _execute_login(self, email, password):
        """Közös segédmetódus az adatok beírására és a kattintásra."""
        self.email_address().send_keys(email)
        self.enter_password().send_keys(password)
        button = self.button_sign_in()
        self.browser.execute_script("arguments[0].click();", button)