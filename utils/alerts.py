from playwright.sync_api import Page, expect
from utils.consts import CONFIRMATION_TYPE

def confirmation_checker(page: Page, the_url,
                         conf_type: CONFIRMATION_TYPE,
                         the_button_to_click,
                         timeout_to_wait,
                         the_dialog_msg,
                         the_result_locator = None,
                         the_result_text= None):

    page.goto(the_url)

    dialog_message = []

    def handle_dialog(dialog):
        dialog_message.append(dialog.message)
        if(conf_type is CONFIRMATION_TYPE.CONF_ACCEPT):
            dialog.accept()  # click OK  (use dialog.dismiss() for Cancel)
        else:
            dialog.dismiss()


    page.on("dialog", handle_dialog)
    page.locator(the_button_to_click).click()

    page.wait_for_timeout(timeout_to_wait)

    # Verify the confirmation message
    assert len(dialog_message) > 0, "No confirmation dialog was triggered"
    assert dialog_message[0] == the_dialog_msg, f"Unexpected dialog message: {dialog_message[0]}"

    # Verify the result text on the page after clicking OK
    if(the_result_locator is not None):
        if(the_result_text == "CheckMe"):
            print("Kuku")
        result = page.locator(the_result_locator)
        assert result.is_visible(), "Result element not found"
        assert result.inner_text() == the_result_text, f"Unexpected result: {result.inner_text()}"
    else:
        pass

def prompt_checker(page: Page,
                   the_url,
                   conf_type: CONFIRMATION_TYPE,
                   the_input_text,
                   the_button_to_click,
                   timeout_to_wait,
                   the_dialog_text,
                   the_dialog_msg,
                   the_result_locator):

    page.goto(the_url)

    dialog_message = []

    def handle_dialog(dialog):
        dialog_message.append(dialog.message)  # capture the prompt question
        if (conf_type == conf_type.CONF_ACCEPT):
            print("Here we are in accept")
            dialog.accept(the_input_text)
        else:
            print("Here we are in dismiss")
            dialog.dismiss()

    page.on("dialog", handle_dialog)
    page.locator(the_button_to_click).click()

    page.wait_for_timeout(timeout_to_wait)

    # Verify the prompt question
    assert len(dialog_message) > 0, "No prompt dialog was triggered"
    assert dialog_message[0] == the_dialog_text, f"Unexpected prompt message: {dialog_message[0]}"

    # Verify the submitted text is reflected on the page
    result = page.locator(the_result_locator)
    assert result.is_visible(), "Result element not found"
    assert result.inner_text().startswith(the_dialog_msg), f"Unexpected result: {result.inner_text()}"