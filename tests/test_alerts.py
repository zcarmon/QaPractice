from utils.alerts import confirmation_checker
from utils.consts import CONFIRMATION_TYPE, BASE_URL_ALERT_CONFIRM
from utils.field_checker import *

def test_alert_box(page: Page):
    confirmation_checker(page,
                         "https://www.qa-practice.com/elements/alert/alert",
                         CONFIRMATION_TYPE.CONF_ACCEPT,
                         '[class="a-button"]',
                         300,
                         "I am an alert!")

def test_confirmation_box_ok(page: Page):
    confirmation_checker(page,
                         BASE_URL_ALERT_CONFIRM,
                         CONFIRMATION_TYPE.CONF_ACCEPT,
                         '[class="a-button"]',
                         300,
                         "Select Ok or Cancel",
                         '[id="result-text"]',
                         "Ok")

def test_confirmation_box_cancel(page: Page):
    confirmation_checker(page,
        BASE_URL_ALERT_CONFIRM,
        CONFIRMATION_TYPE.CONF_CANCEL,
        '[class="a-button"]',
        300,
        "Select Ok or Cancel",
        '[id="result-text"]',
        "Cancel")
