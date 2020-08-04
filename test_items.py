import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    buttons_count = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert buttons_count > 0, "Button add to basket is not found"
