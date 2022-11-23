selenium_path = "/Users/macbookpro/Desktop/Projects/Web-Scrapping/chromedriver"
from selenium.webdriver.chrome.options import Options

def driver_configurations():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--window-size=%s" % '1000,800')
    options.add_experimental_option("detach", True)
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )
    options.add_argument("--disable-notifications")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    return options