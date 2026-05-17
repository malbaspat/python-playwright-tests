import time
import playwright.sync_api
from playwright.sync_api import Playwright
from playwright.sync_api import expect

def test_inventory_page(logged_in_page):
    logged_in_page.goto("https://www.saucedemo.com/inventory.html")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_inventory_page(logged_in_page):
    logged_in_page.goto("https://www.saucedemo.com/inventory.html")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)




