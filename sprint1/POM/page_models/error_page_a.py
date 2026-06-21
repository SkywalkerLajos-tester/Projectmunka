from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ErrorPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.map_locator = (By.ID, "map")

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-404")

    def is_404_displayed(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return error.is_displayed()
        except:
            return False

    def get_error_text(self):
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error.text