from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EmpPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def logout(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "logout")))

    def amount(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "amountInput")))

    def description(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "descriptionInput")))

    def submit(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "reqSubmit")))

    def managerTools(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "managerTools")))

    def pendingTable(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reqViewerBody"]/tr')))

    def reviewedTable(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reqReviewedBody"]/tr')))
