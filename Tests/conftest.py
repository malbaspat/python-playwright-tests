import pytest
from playwright.sync_api import sync_playwright
import pytest
from playwright.sync_api import sync_playwright

WEBPAGE = 'https://www.saucedemo.com/'
USER = ('standard_user')
PASS = ('secret_sauce')

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def open_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(WEBPAGE)
    page.get_by_placeholder('Username').fill(USER)
    page.get_by_placeholder('Password').fill(PASS)
    page.get_by_role("button", name='Login').click()
    context.storage_state(path="auth.json")
    return page

@pytest.fixture
def logged_in_page(browser):
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    yield page
    context.close()





