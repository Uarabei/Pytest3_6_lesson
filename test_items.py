link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_should_see_basket_button(browser):
    browser.get(link)
    basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert basket_button is not None, "Basket button not find"