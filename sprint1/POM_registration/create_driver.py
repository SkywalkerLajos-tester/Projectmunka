from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_configured_chrome_driver():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--guest')
    options.add_argument("--lang=hu")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    return browser
