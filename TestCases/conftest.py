import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope='class')
def setup():
    # Set the path to the ChromeDriver executable
    s = Service("//Users//mac//Downloads//chromedriver_mac_arm64")

    chrome_options = ChromeOptions()
    # Set the user data directory for the Chrome profile
    chrome_options.add_argument("user-data-dir=F:\\testing\\Meta5")
    # Add the extension (metamask.crx) to the Chrome options
    chrome_options.add_extension("/Users/mac/PycharmProjects/MetaMask/metamask.crx")

    # Create the WebDriver instance using the ChromeDriver service and options
    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.get("https://google.com/")

    # Maximize the browser window
    driver.maximize_window()

    yield driver

    # Quit the browser session after all tests are completed
    driver.quit()
