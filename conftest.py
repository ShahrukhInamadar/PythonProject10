import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Important for CI like GitHub Actions
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()
