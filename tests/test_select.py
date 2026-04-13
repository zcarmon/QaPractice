from playwright.sync_api import Page, expect
from utils.consts import FIELD_ID_RESULT_TEXT, BASE_URL_MULT_SELECT


#Check whenever we are in the correct page
def test_main_page(page :Page):
    page.goto(BASE_URL_MULT_SELECT)
    expect(page.locator("h1")).to_have_text('Select inputs')
    pass

#Check the dropdown list selection --> press the Submit button and check the result
def test_dropdown_list(page :Page):
    page.goto(BASE_URL_MULT_SELECT)
    #Consts
    destination = "Mountains"
    transport = "Car"
    when = "Today"
    phrase_template = "to go by <transport> to the <destination> <when>"

    #Select the dropdowns
    page.locator('[name="choose_the_place_you_want_to_go"]').select_option(destination)
    page.locator('[name="choose_how_you_want_to_get_there"]').select_option(transport)
    page.locator('[name="choose_when_you_want_to_go"]').select_option(when)

    #Press the Submit button
    page.get_by_role("button",name = "Submit").click()

    #Prepare the result phrase
    res_txt = phrase_template.replace("<transport>",transport).replace("<destination>",destination).replace("<when>",when).lower()

    #Check if the result is as expected
    expect(page.locator(FIELD_ID_RESULT_TEXT)).to_have_text(res_txt)

    pass