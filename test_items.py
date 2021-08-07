link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_user_should_see_buy_button(browser):
    browser.get(link)
    buy_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert buy_button is not None, "Button not found"
    