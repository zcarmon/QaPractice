from utils.consts import *
from utils.field_checker import *

BASE_URL = "https://www.qa-practice.com/elements/checkbox/"
SINGLE = "single_checkbox"
MULTI = "mult_checkbox"

def test_single(page :Page):
    page.goto(BASE_URL+SINGLE)
    box_locator = page.locator('[class="form-check-label"]')
    if(box_locator.text_content() == "Select me or not"):
        box_locator.uncheck()
        check_result_by_click(page, FIELD_ID_SUBMIT, FIELD_ID_RESULT_TEXT, FIELD_RESULT_EMPTY)

    check_result_by_click(page,FIELD_ID_SUBMIT,FIELD_ID_RESULT_TEXT,FIELD_SUBMITTED)
    pass

