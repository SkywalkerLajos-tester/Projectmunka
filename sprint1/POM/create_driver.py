from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_configured_chrome_driver():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--guest')
    options.add_argument("--lang=hu")

    # Új típusú headless mód (stabilabb a modern Selenium verziókban)
    options.add_argument("--headless=new")

    # --- EZEK A LINUX / CI KÖRNYEZETHEZ KÖTELEZŐEK ---
    options.add_argument("--no-sandbox")  # Megkerüli a Linux sandbox korlátozásokat
    options.add_argument("--disable-dev-shm-usage")  # A /dev/shm memória particionálási hiba ellen
    options.add_argument("--disable-gpu")  # Erőforrás-megtakarítás (CI-ban nincs GPU)

    #options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)
    return browser


# def get_configured_chrome_driver():
#     options = Options()
#     options.add_experimental_option('detach', True)
#     options.add_argument('--guest')
#     options.add_argument("--lang=hu")
#     browser = webdriver.Chrome(options=options)
#     browser.maximize_window()
#     return browser