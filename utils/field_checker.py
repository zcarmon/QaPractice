from playwright.sync_api import Page, expect


def check_field_value_and_result(page :Page,
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

def check_result_by_click(page :Page,
                          field,
                          result_field_name,
                          result_message):

    if(page.locator(field).is_enabled()):
        print("The field is enabled !")
        page.locator(field).click()
        expect(page.locator(result_field_name)).to_have_text(result_message)
    else:
        print("\nATTENTION the field is disabled")

def check_result_on_new_page_by_click(page :Page,
                                      page_url,
                                      context,
                                      field,
                                      result_field_name,
                                      result_message):
    """
    :param page: the page
    :param page_url: the url to be loaded by goto
    :param context: the context
    :param field: the field to be located and clicked
    :param result_field_name: the result field to be located
    :param result_message: the result message
    :return:
    """

    page.goto(page_url)

    with context.expect_page() as new_page_info:
        page.locator(field).click()

    new_page = new_page_info.value

    expect(new_page.locator(result_field_name)).to_have_text(result_message)

    pass