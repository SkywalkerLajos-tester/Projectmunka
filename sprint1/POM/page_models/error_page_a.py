
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ErrorPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.map_locator = (By.ID, "map")

    def is_map_displayed(self):
        maps = self.driver.find_elements(*self.map_locator)
        return len(maps) > 0

    def check_map_bug(self):
        is_map = self.is_map_displayed()

        if is_map:
            print("Az oldal NEM az elvárt módon működik: a térkép megjelenik, pedig nem lenne szabad!")
        else:
            print(" Az oldal az elvárás szerint működik: nincs térkép találat nélkül.")

        return is_map

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