import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The user is on the login page')
def step_impl(context):
    driver: WebDriver = context.driver
    # domain = os.getenv("DOMAIN")
    # driver.get(domain+"/index.html")
    driver.get("F:/PycharmProjects/Project1/Project1Web/web/index.html")


@when(u'The user enters {username} into the username field')
def step_impl(context, username: str):
    context.login_page.username().send_keys(username)


@when(u'The user enters {password} into the password field')
def step_impl(context, password: str):
    context.login_page.password().send_keys(password)


@when(u'The user clicks on the login button')
def step_impl(context):
    context.login_page.login().click()


@then(u'The title should be {title}')
def step_impl(context, title: str):
    time.sleep(1)  # will need to be longer for slower systems. My system works at t=.5 with moderate pc specs
    assert context.driver.title == title
