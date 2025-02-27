import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from locators import *
from options import *

options = Options()
options.add_argument(WINDOW_SIZE)
options.add_argument(BLINK_ENGINE_DISABLE)
options.add_argument(USER_AGENT)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get(URL)


def wwait(*args):
    '''
    Просто хотел сократить количество кода, вот и сделал функцию под самые частые строчки
    '''
    if len(args) == 1:
        web_element = args[0]
        wait.until(EC.element_to_be_clickable(web_element)).click()
        time.sleep(3)
    elif len(args) == 2:
        web_element, keys = args
        wait.until(EC.element_to_be_clickable(web_element)).send_keys(keys)
        time.sleep(3)
    else:
        raise ValueError("Too many arguments, expect one or two.")


# Authorization as standard user
wwait(INPUT_USERNAME, LOGIN)
wwait(INPUT_PASSWORD, PASSWORD)
wwait(LOGIN_BUTTON)
time.sleep(3)
