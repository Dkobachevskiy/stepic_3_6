link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_basket_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), 'basket button not found'
