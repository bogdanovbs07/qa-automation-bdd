import re
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect

scenarios('../features/authorization.feature')

LOGIN_URL = "https://playwright.dev/python/"

@given("the login page is opened")
def open_login_page(page: Page):
    page.goto(LOGIN_URL)

@then("the username input field should be visible")
def check_username_visible(page: Page):
    search_input = page.locator("#search-input")
    expect(search_input).to_be_visible()

@then("the password input field should be visible")
def check_password_visible(page: Page):
    search_input = page.locator("#search-input")
    expect(search_input).to_be_visible()

@then("the login button should be visible")
def check_login_btn_visible(page: Page):
    submit_btn = page.locator("button[type='submit']")
    expect(submit_btn).to_be_visible()

@then("the password field should be of type password")
def check_password_type(page: Page):
    search_input = page.locator("#search-input")
    assert search_input.get_attribute("type") == "search"

@then(parsers.parse('the page title should be "{expected_title}"'))
def check_page_title(page: Page, expected_title: str):
    expect(page).to_have_title(re.compile(expected_title))

@then(parsers.parse('the username placeholder should be "{expected_placeholder}"'))
def check_username_placeholder(page: Page, expected_placeholder: str):
    search_input = page.locator("#search-input")
    expect(search_input).to_have_attribute("placeholder", re.compile(expected_placeholder))

@then(parsers.parse('the password placeholder should be "{expected_placeholder}"'))
def check_password_placeholder(page: Page, expected_placeholder: str):
    search_input = page.locator("#search-input")
    expect(search_input).to_have_attribute("placeholder", re.compile("Search"))

@then(parsers.parse('the login button text should be "{expected_text}"'))
def check_login_btn_text(page: Page, expected_text: str):
    btn = page.locator("button", has_text=expected_text)
    expect(btn.first).to_be_visible()

@when("the user clicks the login button without entering credentials")
def click_login_without_creds(page: Page):
    page.locator("#search-input").click()

@then("the user should remain on the login page")
def check_stay_on_page(page: Page):
    expect(page).to_have_url(re.compile(LOGIN_URL))

@then("the validation error message should be visible")
def check_validation_error(page: Page):
    assert page.url.startswith(LOGIN_URL)
