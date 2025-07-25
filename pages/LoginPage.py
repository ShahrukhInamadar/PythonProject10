from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Define locators as class attributes (optional, can be inside methods too)
    Username = (By.XPATH, "//input[@id='username']")
    Password = (By.XPATH, "//input[@id='password']")
    Submit_btn = (By.XPATH, "//button[@id='submit']")
    Success_message = (By.XPATH, "//*[text()='Logged In Successfully']")

    def enter_user_name(self, username):
        self.do_send_keys(self.Username, username)

    def enter_the_password(self, password):
        self.do_send_keys(self.Password, password)

    def click_on_submit(self):
        self.do_click(self.Submit_btn)

    def get_succeess_message(self):
        return self.get_the_element(self.Success_message)
