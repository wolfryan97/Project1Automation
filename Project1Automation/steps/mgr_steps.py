import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

@given(u'The User is on the manager tools page')
def step_impl(context):
    driver: WebDriver = context.driver
    # domain = os.getenv("DOMAIN")
    # driver.get(domain+"/mgrPage.html")
    driver.get("F:/PycharmProjects/Project1/Project1Web/web/mgrPage.html")


@when(u'The User enters manager comment {comment} into the manager comment textarea {name}')
def step_impl(context, comment: str, name: str):
    context.mgr_page.mgr_comment(name).send_keys(comment)


@when(u'The User clicks the button {button}')
def step_impl(context, button: str):
    context.mgr_page.button(button).click()


@when(u'The User clicks the back button')
def step_impl(context):
    context.mgr_page.back().click()


@then(u'The resolved table\'s size should be {size}')
def step_impl(context, size: str):
    time.sleep(.25)
    assert len(context.emp_page.reviewedTable()) == int(size)


@when(u'The User clicks on the View Statistics button')
def step_impl(context):
    context.mgr_page.view_statistics().click()

