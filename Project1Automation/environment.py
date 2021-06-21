from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.emp_page import EmpPage
from poms.login_page import LoginPage
from behave.runner import Context

from poms.mgr_page import MgrPage
from poms.statistics_page import StatisticsPage


def before_all(context: Context):
    context.driver: WebDriver = webdriver.Chrome('C:\\Users\\Wolf\\Desktop\\drivers\\chromedriver.exe')
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.emp_page = EmpPage(context.driver)
    context.mgr_page = MgrPage(context.driver)
    context.statistics_page = StatisticsPage(context.driver)
    print("I run before any scenarios")


def after_all(context):
    print("I run after any scenarios")
    context.driver.quit()
