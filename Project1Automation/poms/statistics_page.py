from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class StatisticsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def back(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "back")))

    def logout(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "logout")))

    def piechart(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "piechart")))

    def columnchart(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "columnchart")))
