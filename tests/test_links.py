from utils.consts import *
from utils.field_checker import *

""" Test a new tab opened by click on a link """
def test_new_tab_link(page :Page, context ):

    result_on_new_page_by_click_checker(page,
                                      "https://www.qa-practice.com/elements/new_tab/link",
                                        context,
                                        HREF_NEW_PAGE,
                                        FIELD_ID_RESULT_TEXT,
                                        FIELD_NEW_PAGE_IN_NEW_TAB)

""" Test a new tab opened by click on a button """
def test_new_tab_button(page :Page, context ):

    result_on_new_page_by_click_checker(page,
                                      "https://www.qa-practice.com/elements/new_tab/button",
                                        context,
                                        HREF_NEW_PAGE,
                                        FIELD_ID_RESULT_TEXT,
                                        FIELD_NEW_PAGE_IN_NEW_TAB)