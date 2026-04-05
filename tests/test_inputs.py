from playwright.sync_api import Page, expect

from utils.consts import *
from utils.field_checker import check_field_value_and_result

BASE_URL = "https://www.qa-practice.com/elements/input/simple"

def test_input_field_seq(page :Page):
    page.goto(BASE_URL)
    page.locator(FIELD_NAME_TEXT_STRING).press_sequentially("This is my home work !",delay=200)
    pass

def test_input_field_fill(page :Page):
    page.goto(BASE_URL)
    page.locator(FIELD_NAME_TEXT_STRING).fill("This is my home work !")
    pass

# 1. Go to the email page
# 2. Enter an invalid email and check the error msg
# 3. Enter a valid email
def test_input_email(page :Page):
    page.goto(BASE_URL)
    page.locator('[href="/elements/input/email"]').click()
    expect(page.locator(FIELD_NAME_EMAIL))

    #Check an invalid mail address
    check_field_value_and_result(page,
                                 FIELD_NAME_EMAIL,
                                 "kuku@x",
                                 PRESS_SEQ_DELAY,
                                 '[id="error_1_id_email"]',
                                 'Enter a valid email address.')

    # Check a valid mail address
    check_field_value_and_result(page,
                 FIELD_NAME_EMAIL,
                 "kuku@x.com",
                 PRESS_SEQ_DELAY,
                 FIELD_ID_RESULT_TEXT,
                 'kuku@x.com',
                 True)

    pass