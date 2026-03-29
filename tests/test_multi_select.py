from playwright.sync_api import Page, expect

BASE_URL = "https://www.qa-practice.com/elements/select/mult_select"

def test_main_page(page :Page):
    page.goto(BASE_URL)
    expect(page.locator("h1").text_content("Select inputs"))
    pass

