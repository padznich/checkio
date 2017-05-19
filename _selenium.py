"""
Preconf
mv geckodriver /usr/bin/
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 15)
    return driver


def checkio_click_start_game(_driver):

    uri = "https://py.checkio.org/"

    _driver.get(uri)

    try:
        start_game = _driver.wait.until(Ec.element_to_be_clickable(
            (By.XPATH, "//a[@href='/login/checkio/']")))
        start_game.click()
    except TimeoutException:
        print("Start game click Failed.")


def checkio_login(_driver, _username=None, _password=None):

    try:
        customer_form = _driver.wait.until(Ec.presence_of_element_located(
            (By.NAME, "username")))
        password_form = _driver.wait.until(Ec.presence_of_element_located(
            (By.NAME, "password")))
        button = _driver.wait.until(Ec.element_to_be_clickable(
            (By.XPATH, "//input[@class='auth__btn']")))
        customer_form.send_keys(_username)
        password_form.send_keys(_password)
        button.click()
    except TimeoutException:
        print("Login Failed.")


def checkio_click_home(_driver):

    try:
        start_game = _driver.wait.until(Ec.element_to_be_clickable(
            (By.XPATH, "//a[@href='/station/home/']")))
        start_game.click()
    except TimeoutException:
        print("Home click Failed.")


if __name__ == "__main__":

    d = init_driver()

    checkio_click_start_game(d)
    checkio_login(d)
    checkio_click_home(d)

    # time.sleep(5)
    # d.quit()
