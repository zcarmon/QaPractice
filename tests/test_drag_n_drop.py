from playwright.sync_api import Page

def test_drag_n_drop_box(page : Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
