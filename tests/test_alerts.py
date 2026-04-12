from utils.alerts import *
from utils.consts import *
from utils.field_checker import *

""" Testing an alert popup """
def test_alert_box(page: Page):

    confirmation_checker(page,
                         "https://www.qa-practice.com/elements/alert/alert",
                         CONFIRMATION_TYPE.CONF_ACCEPT,
                         FIELD_CLASS_A_BUTTON,
                         PAGE_WAIT_TIMEOUT_IN_MSEC,
                         "I am an alert!")

""" Testing confirmation box """
def test_confirmation_box_ok(page: Page):

    confirmation_checker(page,
                         BASE_URL_ALERT_CONFIRM,
                         CONFIRMATION_TYPE.CONF_ACCEPT,
                         FIELD_CLASS_A_BUTTON,
                         PAGE_WAIT_TIMEOUT_IN_MSEC,
                         "Select Ok or Cancel",
                         FIELD_ID_RESULT_TEXT,
                         "Ok")

""" Testing confirmation box by pressing Cancel"""
def test_confirmation_box_cancel(page: Page):

    confirmation_checker(page,
        BASE_URL_ALERT_CONFIRM,
        CONFIRMATION_TYPE.CONF_CANCEL,
        FIELD_CLASS_A_BUTTON,
        PAGE_WAIT_TIMEOUT_IN_MSEC,
        "Select Ok or Cancel",
        FIELD_ID_RESULT_TEXT,
        "Cancel")

def test_prompt_accept(page: Page):

    prompt_checker(page,
                   BASE_URL_ALERT_PROMPT,
                   CONFIRMATION_TYPE.CONF_ACCEPT,
                   "kuku",
                   FIELD_CLASS_A_BUTTON,
                   PAGE_WAIT_TIMEOUT_IN_MSEC,
                   DIALOG_TEXT_PLEASE_ENTER_SOME_TEXT,
                   "You entered",
                   FIELD_ID_RESULT)

def test_prompt_accept_without_text(page: Page):

    prompt_checker(page,
                   BASE_URL_ALERT_PROMPT,
                   CONFIRMATION_TYPE.CONF_ACCEPT,
                   EMPTY_STRING,
                   FIELD_CLASS_A_BUTTON,
                   PAGE_WAIT_TIMEOUT_IN_MSEC,
                   DIALOG_TEXT_PLEASE_ENTER_SOME_TEXT,
                   "You entered",
                   FIELD_ID_RESULT)

def test_prompt_cancel(page: Page):
    prompt_checker(page,
                   BASE_URL_ALERT_PROMPT,
                   CONFIRMATION_TYPE.CONF_CANCEL,
                   EMPTY_STRING,
                   FIELD_CLASS_A_BUTTON,
                   PAGE_WAIT_TIMEOUT_IN_MSEC,
                   DIALOG_TEXT_PLEASE_ENTER_SOME_TEXT,
                   "You canceled the prompt",
                   FIELD_ID_RESULT)