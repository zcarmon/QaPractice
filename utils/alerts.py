from playwright.sync_api import Page, expect
from utils.consts import CONFIRMATION_TYPE, EVENT_DIALOG

def confirmation_checker(page: Page, url,
                         conf_type: CONFIRMATION_TYPE,
                         button_to_click,
                         timeout_to_wait,
                         dialog_msg,
                         result_locator = None,
                         result_text= None):

    page.goto(url)

    dialog_message = []

    """ Click the relevant button according to the request """
    def handle_dialog(dialog):
        dialog_message.append(dialog.message)
        if(conf_type is CONFIRMATION_TYPE.CONF_ACCEPT):
            dialog.accept()  # click OK  (use dialog.dismiss() for Cancel)
        else:
            dialog.dismiss()

    page.on(EVENT_DIALOG, handle_dialog)
    page.locator(button_to_click).click()

    page.wait_for_timeout(timeout_to_wait)

    # Verify the confirmation message
    assert len(dialog_message) > 0, "No confirmation dialog was triggered"
    assert dialog_message[0] == dialog_msg, f"Unexpected dialog message: {dialog_message[0]}"

    # Verify the result text on the page after clicking OK
    if(result_locator is not None):
        #if(result_text == "CheckMe"):
        #    print("Kuku")
        result = page.locator(result_locator)
        assert result.is_visible(), "Result element not found"
        assert result.inner_text() == result_text, f"Unexpected result: {result.inner_text()}"
    else:
        pass

def prompt_checker(page: Page,
                   url,
                   conf_type: CONFIRMATION_TYPE,
                   input_text,
                   button_to_click,
                   timeout_to_wait,
                   dialog_text,
                   dialog_msg,
                   result_locator):

    page.goto(url)

    dialog_message = []

    def handle_dialog(dialog):
        dialog_message.append(dialog.message)  # capture the prompt question
        if (conf_type == conf_type.CONF_ACCEPT):
            print("Here we are in accept")
            dialog.accept(input_text)
        else:
            print("Here we are in dismiss")
            dialog.dismiss()

    page.on(EVENT_DIALOG, handle_dialog)
    page.locator(button_to_click).click()

    page.wait_for_timeout(timeout_to_wait)

    # Verify the prompt question
    assert len(dialog_message) > 0, "No prompt dialog was triggered"
    assert dialog_message[0] == dialog_text, f"Unexpected prompt message: {dialog_message[0]}"

    # Verify the submitted text is reflected on the page
    result = page.locator(result_locator)
    assert result.is_visible(), "Result element not found"
    assert result.inner_text().startswith(dialog_msg), f"Unexpected result: {result.inner_text()}"