from playwright.sync_api import Page, expect


def field_value_and_result_checker(page :Page,
                                   field,
                                   value,
                                   press_seq_delay,
                                   result_field_name,
                                   result_message,
                                   clear_field=False):
    if clear_field:
        page.locator(field).clear()

    page.locator(field).press_sequentially(value, delay=press_seq_delay)
    page.locator(field).press("Enter")
    expect(page.locator(result_field_name)).to_have_text(result_message)

def check_result_by_click(page :Page,
                          field,
                          result_field_name,
                          result_message):

    page.locator(field).click()
    expect(page.locator(result_field_name)).to_have_text(result_message)

def result_by_click_checker(page :Page,
                            field,
                            result_field_name,
                            result_message):

    if(page.locator(field).is_enabled()):
        print("The field is enabled !")
        page.locator(field).click()
        expect(page.locator(result_field_name)).to_have_text(result_message)
    else:
        print("\nATTENTION the field is disabled")

def result_on_new_page_by_click_checker(page :Page,
                                        page_url,
                                        context,
                                        field,
                                        result_field_name,
                                        result_message):

    page.goto(page_url)

    with context.expect_page() as new_page_info:
        page.locator(field).click()

    new_page = new_page_info.value

    expect(new_page.locator(result_field_name)).to_have_text(result_message)

    pass