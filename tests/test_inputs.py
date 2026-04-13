from playwright.sync_api import Page, expect
from utils.consts import *
from utils.field_checker import field_value_and_result_checker

""" Test filling a simple field sequentially """
def test_input_field_seq(page :Page):
    page.goto(BASE_URL_INPUT_SIMPLE)
    page.locator(FIELD_NAME_TEXT_STRING).press_sequentially("This is my home work !",delay=200)
    pass

""" Test filling a simple field like copy paste """
def test_input_field_fill(page :Page):
    page.goto(BASE_URL_INPUT_SIMPLE)
    page.locator(FIELD_NAME_TEXT_STRING).fill("This is my additional home work !")
    pass

""" Test filling an e-mail """
# 1. Go to the email page
# 2. Enter an invalid email and check the error msg
# 3. Enter a valid email
def test_input_email(page :Page):
    page.goto(BASE_URL_INPUT_SIMPLE)
    page.locator('[href="/elements/input/email"]').click()
    expect(page.locator(FIELD_NAME_EMAIL))

    #Check an invalid mail address
    field_value_and_result_checker(page,
                                   FIELD_NAME_EMAIL,
                                 "kuku@x",
                                   PRESS_SEQ_DELAY,
                                 '[id="error_1_id_email"]',
                                 'Enter a valid email address.')

    # Check a valid mail address
    field_value_and_result_checker(page,
                                   FIELD_NAME_EMAIL,
                 "correct@mail.com",
                                   PRESS_SEQ_DELAY,
                                   FIELD_ID_RESULT_TEXT,
                 'correct@mail.com',
                                   True)

    pass