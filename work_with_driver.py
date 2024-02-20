from selenium import webdriver


def connect_to_browser(link):
    my_driver = webdriver.Chrome()
    my_driver.implicitly_wait(10)
    my_driver.get(link)
    return my_driver


def quit_browser(opened_driver):
    opened_driver.close()
    opened_driver.quit()