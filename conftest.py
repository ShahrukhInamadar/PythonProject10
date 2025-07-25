import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def init_driver():
    chrome_options = Options()
    # Path to the manually downloaded ChromeDriver
    service = Service("C:/WebDriver/chromedriver.exe")  # <-- IMPORTANT

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()
