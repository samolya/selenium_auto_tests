from selenium.webdriver.common.by import By


def test_check_btn_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    target_btn = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert target_btn, "Btn add_to_basket is not found"


