from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MgrPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def back(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "back")))

    def view_statistics(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "viewStatistics")))

    def logout(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "logout")))

    def mgr_comment(self, name: str):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, name)))

    def button(self, name: str):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, name)))
