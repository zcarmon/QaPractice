from playwright.sync_api import Page

def drag_n_drop_checker(page: Page,
                        url,
                        source,
                        target,
                        wait_timeout_in_msec,
                        result_text,
                        drag_obj_locator = None,
                        drop_back = False):

    page.goto(url)

    # Locate the source and target elements
    source = page.locator(source)
    target = page.locator(target)

    # Verify initial state
    assert source.is_visible(), "Source element not found"
    assert target.is_visible(), "Target element not found"

    # Perform drag and drop
    if(not drop_back):
        source.drag_to(target)
    else:
        source.locator(drag_obj_locator).drag_to(target)

    page.wait_for_timeout(wait_timeout_in_msec)

    """ For debug purpose """
    print("\nThis is the full inner text = '" + target.inner_text()+ "'")
    # Verify the result after drop
    if (not drop_back):
        assert target.inner_text().startswith(result_text), f"Unexpected result: {target.inner_text()}"
    else:
        # --- First drag: source → target ---
        assert target.inner_text().startswith(result_text), "Target drag failed"
        assert source.inner_text() == "", "Source should be empty after first drag"

        # --- Second drag: target → source (drag it back) ---
        target.locator(drag_obj_locator).drag_to(source)
        assert source.inner_text().startswith(result_text), "Source drag failed"
        assert target.inner_text() == "", "Target should be empty after second drag"

        page.wait_for_timeout(wait_timeout_in_msec)