link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_for_adding_to_basket(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector('.btn-add-to-basket')
