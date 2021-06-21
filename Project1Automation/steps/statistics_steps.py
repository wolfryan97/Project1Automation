import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

@given(u'The User is on the statistics page')
def step_impl(context):
    driver: WebDriver = context.driver
    # domain = os.getenv("DOMAIN")
    # driver.get(domain+"/statistics.html")
    driver.get("F:/PycharmProjects/Project1/Project1Web/web/statistics.html")


@then(u'The Pie Chart exists')
def step_impl(context):
    assert context.statistics_page.piechart() is not None


@then(u'The Vertical Bar Graph exists')
def step_impl(context):
    assert context.statistics_page.columnchart() is not None
