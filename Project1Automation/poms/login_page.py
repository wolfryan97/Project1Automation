from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        element: WebElement = self.driver.find_element_by_id("username")
        return element

    def password(self):
        element: WebElement = self.driver.find_element_by_id("password")
        return element

    def login(self):
        element: WebElement = self.driver.find_element_by_id("submitBtn")
        return element
