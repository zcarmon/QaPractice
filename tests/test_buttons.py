from utils.consts import *
from utils.field_checker import *

def test_simple(page :Page):
    page.goto(BASE_URL_BUTTON_SIMPLE)
    page.locator('[href = "/elements/button/simple"]').click()
    check_result_by_click(page,FIELD_ID_SUBMIT,FIELD_ID_RESULT_TEXT,FIELD_SUBMITTED)
    pass

def test_looks_like(page: Page):
    page.goto(BASE_URL_BUTTON_SIMPLE)
    page.locator('[href = "/elements/button/like_a_button"]').click()
    check_result_by_click(page, FIELD_CLASS_A_BUTTON, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass

def test_disabled(page: Page):
    page.goto(BASE_URL_BUTTON_SIMPLE)
    page.locator('[href = "/elements/button/disabled"]').click()
    check_result_by_click(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    page.locator(FIELD_ID_SELECT_STATE).select_option(FIELD_ENABLED)
    check_result_by_click(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass