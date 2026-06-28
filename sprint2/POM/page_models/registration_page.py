from sprint1.POM.general_page import GeneralPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class RegistrationPage(GeneralPage):
    def __init__(self, browser, URL):
        super().__init__(browser, URL)
        self.wait = WebDriverWait(self.browser, 10)

    def last_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "lastName")))

    def first_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "firstName")))

    def phone_number(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "phoneNumber")))

    def email(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='email'])[2]")))

    def confirm_email(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "confirmEmail")))

    def password(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='password'])[2]")))

    def confirm_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "confirmPassword")))

    def button_registration(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='submit'])[2]")))

    def registration_text(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Registration']")))


##################ERROR MESSAGES#################################x

    def error_last_name(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[1]/small")))

    def error_first_name(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[2]/small")))

    def error_phone_number(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[3]/small")))

    def error_email_missing_or_wrong_single(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[4]/small")))

    def error_email_wrong_format(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[4]/small[2]")))

    def error_confirm_email(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Email does not match')]")))

    def error_password(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[6]/small")))

    def error_confirm_password(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[7]/small")))


#################Sending classes#################################x

    def successful_registration_without_error(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div/form[@class='main-form ng-dirty ng-touched ng-valid ng-submitted']")))

    def successful_registration_with_error(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div/form[@class='main-form ng-invalid ng-dirty ng-touched ng-submitted']")))

    def unsuccessful_registration(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div/form[contains(@class, 'ng-invalid')]")))

