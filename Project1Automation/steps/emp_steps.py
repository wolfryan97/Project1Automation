import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The User is on the employee page')
def step_impl(context):
    driver: WebDriver = context.driver
    # domain = os.environ.get('DOMAIN')  # also able to set/use domain environ var
    # driver.get(domain+"/empPage.html")
    driver.get("F:/PycharmProjects/Project1/Project1Web/web/empPage.html")


@when(u'The User enters an amount {amount}')
def step_impl(context, amount: str):
    context.emp_page.amount().send_keys(amount)


@when(u'The User enters a description {description}')
def step_impl(context, description: str):
    context.emp_page.description().send_keys(description)


@when(u'The User clicks the submit button')
def step_impl(context):
    context.emp_page.submit().click()


@when(u'The User clicks the logout button')
def step_impl(context):
    context.emp_page.logout().click()


@then(u'Then The title should be Login Page')
def step_impl(context):
    assert context.driver.title == "Login Page"


@then(u'The pending table\'s size should be {size}')
def step_impl(context, size: str):
    time.sleep(.25)
    assert len(context.emp_page.pendingTable()) == int(size)


@when(u'The User clicks the alert \'OK\' button')
def step_impl(context):
    #time.sleep(.5)
    a = context.driver.switch_to.alert
    a.accept()


@then(u'The amount textbox should be empty')
def step_impl(context):
    time.sleep(.25)
    assert context.emp_page.amount().get_attribute('value') == ""


@then(u'The description textarea should be empty')
def step_impl(context):
    time.sleep(.25)
    assert context.emp_page.description().get_attribute('value') == ""


@when(u'The User clicks on the Manager Tools button')
def step_impl(context):
    context.emp_page.managerTools().click()


@then(u'An alert box should say {alert_box}')
def step_impl(context, alert_box: str):
    time.sleep(1)
    a = context.driver.switch_to.alert
    assert a.text == alert_box
