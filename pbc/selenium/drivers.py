from selenium.webdriver.android import webdriver
from pbc.selenium.base_driver import BaseDriver


class FirefoxDriver(BaseDriver):

    def __init__(self):
        self._driver = webdriver.Firefox()
