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

def check_result_on_new_page_by_click(page :Page,
                                      the_page_url,
                                      context,
                                      the_field,
                                      the_result_field_name,
                                      the_result_message):
    """
    :param page: the page
    :param the_page_url: the url to be loaded by goto
    :param context: the context
    :param the_field: the field to be located and clicked
    :param the_result_field_name: the result field to be located
    :param the_result_message: the result message
    :return:
    """

    page.goto(the_page_url)

    with context.expect_page() as new_page_info:
        page.locator(the_field).click()

    new_page = new_page_info.value

    expect(new_page.locator(the_result_field_name)).to_have_text(the_result_message)

    pass