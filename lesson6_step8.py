import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from formula import get_res
from work_with_driver import connect_to_browser, quit_browser
from work_with_stepik import login_to_site, send_answer


link_to_get_code = "http://suninjuly.github.io/explicit_wait2.html"
link_to_send_answer = "https://stepik.org/lesson/181384/step/8?unit=156009"


def get_code(my_driver):
    book_btn = WebDriverWait(driver_to_get_code, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button#book")))

    WebDriverWait(driver_to_get_code, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))

    book_btn.click()

    book_btn.location_once_scrolled_into_view

    x = driver_to_get_code.find_element(By.XPATH, "//span[@id='input_value']").text
    res = get_res(int(x))

    input_form = driver_to_get_code.find_element(By.XPATH, "//input[@id='answer']")
    input_form.send_keys(res)

    submit_btn = driver_to_get_code.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()

    alert = driver_to_get_code.switch_to.alert
    alert_text = alert.text.split(": ")[-1]
    return alert_text


try:
    driver_to_get_code = connect_to_browser(link_to_get_code)
    answer = get_code(driver_to_get_code)

    if answer:
        driver_to_send_answer = connect_to_browser(link_to_send_answer)
        login_to_site(my_driver=driver_to_send_answer, login="your_login_to_stepic", password="your_password_to_stepic")
        send_answer(my_driver=driver_to_send_answer, answer=answer)

except Exception as e:
    print(f"Oops, something went wrong! {e}")

finally:
    time.sleep(3)
    quit_browser(driver_to_get_code)
    quit_browser(driver_to_send_answer)
