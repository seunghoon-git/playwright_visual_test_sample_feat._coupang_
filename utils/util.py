import time
from playwright.sync_api import Page

def page_scroll_down(page: Page, scroll_count = 1):
    prev_page_height = page.evaluate("$(document).height()")

    if scroll_count == -1:
        while True:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)

            cur_page_height = page.evaluate("$(document).height()")

            if cur_page_height > prev_page_height:
                prev_page_height = cur_page_height
            elif cur_page_height == prev_page_height:
                break
    elif scroll_count > 0:
        for i in range(scroll_count):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)

    return page