import pytest
from playwright.sync_api import sync_playwright

WEBPAGE = 'https://www.google.com/'

@pytest.fixture
def open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(WEBPAGE)


