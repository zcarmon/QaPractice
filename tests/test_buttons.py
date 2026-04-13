from utils.consts import *
from utils.field_checker import *

""" Test a simple button """
def test_simple(page :Page):
    page.goto(BASE_URL_BUTTON_SIMPLE)
    page.locator('[href = "/elements/button/simple"]').click()
    result_by_click_checker(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass

""" Test a link looks like a button """
def test_looks_like(page: Page):
    page.goto(BASE_URL_BUTTON_SIMPLE)
    page.locator('[href = "/elements/button/like_a_button"]').click()
    result_by_click_checker(page, FIELD_CLASS_A_BUTTON, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass

""" Test when a button is disabled """
def test_disabled(page: Page):
    page.goto(BASE_URL_BUTTON_SIMPLE)
    page.locator('[href = "/elements/button/disabled"]').click()
    result_by_click_checker(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    page.locator(FIELD_ID_SELECT_STATE).select_option(FIELD_ENABLED)
    result_by_click_checker(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_SUBMITTED)
    pass