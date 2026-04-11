FIELD_NAME_EMAIL = '[name="email"]'
FIELD_NAME_TEXT_STRING = '[name="text_string"]'
FIELD_ID_RESULT_TEXT = '[id="result-text"]'
FIELD_ID_SUBMIT = '[id="submit-id-submit"]'
HREF_NEW_PAGE = '[href="/elements/new_tab/new_page"]'
FIELD_ID_RESULT = '[id="result"]'
FIELD_RESULT = "result"
FIEL_ID_CONTENT = '[id="content"]'

FIELD_SUBMITTED = "Submitted"
FIELD_NEW_PAGE_IN_NEW_TAB = "I am a new page in a new tab"
FIELD_RESULT_EMPTY = ""

FIELD_CLASS_A_BUTTON = '[class="a-button"]'

PRESS_SEQ_DELAY = 200 #: Defines the sequential press delay

ROLE_CHECKBOX = "checkbox"

from enum import Enum
class CONFIRMATION_TYPE(Enum):
    CONF_ACCEPT = "accept"
    CONF_CANCEL = "cancel"

DIALOG_TEXT_PLEASE_ENTER_SOME_TEXT = "Please enter some text"

PAGE_WAIT_TIMEOUT_IN_MSEC = 300

EMPTY_STRING = ""

BASE_URL_ALERT_CONFIRM = "https://www.qa-practice.com/elements/alert/confirm"
BASE_URL_ALERT_PROMPT = "https://www.qa-practice.com/elements/alert/prompt"