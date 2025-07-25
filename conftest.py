import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 👈 Important

@pytest.fixture(scope="function")
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Needed for GitHub Actions
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()
