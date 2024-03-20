from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login_to_site(my_driver, login, password):
    enter_btn = my_driver.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
    enter_btn.click()

    my_driver.find_element(By.CSS_SELECTOR, "input#id_login_email").send_keys(login)
    my_driver.find_element(By.CSS_SELECTOR, "input#id_login_password").send_keys(password)

    submit_btn = my_driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    submit_btn.click()

    # continues_btn = WebDriverWait(my_driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.button")))
    # continues_btn.click()


def send_answer(my_driver, answer):

    try:
        input_form = my_driver.find_element(By.CSS_SELECTOR, "textarea.textarea")
        input_form.send_keys(answer)

        submit_btn = my_driver.find_element(By.CSS_SELECTOR, "button.submit-submission")
        submit_btn.click()

    except Exception as e:
        print(f"Oops, something went wrong! {e}")
