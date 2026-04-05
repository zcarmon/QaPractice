from utils.consts import *
from utils.field_checker import *

BASE_URL = "https://www.qa-practice.com/elements/button/simple"

def test_simple(page :Page):
    page.goto(BASE_URL)
    page.locator('[href = "/elements/button/simple"]').click()
    check_result_by_click(page,FIELD_ID_SUBMIT,FIELD_ID_RESULT_TEXT,FIELD_SUBMITTED)
    pass

def test_looks_like(page: Page):
    page.goto(BASE_URL)
    page.locator('[href = "/elements/button/like_a_button"]').click()
    check_result_by_click(page, '[class="a-button"]', FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass

def test_disabled(page: Page):
    page.goto(BASE_URL)
    page.locator('[href = "/elements/button/disabled"]').click()
    check_result_by_click(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    page.locator('[id="id_select_state"]').select_option("Enabled")
    check_result_by_click(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass