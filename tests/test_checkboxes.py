from utils.consts import *
from utils.field_checker import *

BASE_URL = "https://www.qa-practice.com/elements/checkbox/"
SINGLE = "single_checkbox"
MULTI = "mult_checkbox"

def test_single_unchecked(page :Page):
    page.goto(BASE_URL+SINGLE)
    box_locator = page.locator('[class="form-check-label"]')
    box_locator.uncheck()
    page.locator(FIELD_ID_SUBMIT).click()
    expect(page.locator('[id="content"]')).not_to_have_id("result")

def test_single_checked(page: Page):
    page.goto(BASE_URL + SINGLE)
    box_locator = page.locator('[class="form-check-label"]')
    box_locator.check()
    page.locator(FIELD_ID_SUBMIT).click()
    expect(page.locator(FIELD_ID_RESULT_TEXT)).to_have_text("Select me or not", ignore_case=True)

def test_multi_unchecked(page: Page):
    page.goto(BASE_URL + MULTI)
    box_locator = page.locator('[class="form-check form-check-inline"]').get_by_role("checkbox")
    i = 0
    while i < box_locator.count(): #checkbox in box_locator:
        box_locator.nth(i).uncheck()
        i = i + 1

    page.locator(FIELD_ID_SUBMIT).click()
    expect(page.locator('[id="content"]')).not_to_have_id("result")

def test_multi_checked(page: Page):
    #access the url
    page.goto(BASE_URL + MULTI)
    #find the checkboxes
    box_locator = page.locator('[class="form-check form-check-inline"]').get_by_role("checkbox")
    i = 0
    res_text = ""
    #loop over all the checkboxes
    while i < box_locator.count():  # checkbox in box_locator:
        box_locator.nth(i).check()
        #the result is the concatenation of the checkbox's inner text
        res_text = res_text + page.locator('label[for="id_checkboxes_' + str(i) + '"]').inner_text().strip().lower() + ", "
        i = i + 1

    #click the button
    page.locator(FIELD_ID_SUBMIT).click()
    #check the expected result
    expect(page.locator('[id="content"]')).not_to_have_id("result")