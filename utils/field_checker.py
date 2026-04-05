import pytest
from playwright.sync_api import Page, expect

def check_field_value_and_result(page :Page,
                                 the_field,
                                 the_value,
                                 press_seq_delay,
                                 the_result_field_name,
                                 the_result_message,
                                 clear_the_field=False):
    if clear_the_field:
        page.locator(the_field).clear()

    page.locator(the_field).press_sequentially(the_value, delay=press_seq_delay)
    page.locator(the_field).press("Enter")
    expect(page.locator(the_result_field_name)).to_have_text(the_result_message)

def check_result_by_click(page :Page,
                          the_field,
                          the_result_field_name,
                          the_result_message):

    page.locator(the_field).click()
    expect(page.locator(the_result_field_name)).to_have_text(the_result_message)

def check_result_by_click(page :Page,
                          the_field,
                          the_result_field_name,
                          the_result_message):

    if(page.locator(the_field).is_enabled()):
        print("The field is enabled !")
        page.locator(the_field).click()
        expect(page.locator(the_result_field_name)).to_have_text(the_result_message)
    else:
        print("\nATTENTION the field is disabled")
