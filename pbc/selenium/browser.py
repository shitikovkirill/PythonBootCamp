import typing
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pbc.selenium.pages import Page
from pbc.selenium.base_driver import BaseDriver


class FirefoxBrowser(BaseDriver):

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self._driver = webdriver.Remote(
            command_executor='http://192.168.33.10:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox'},
            options=options
        )

    def get_page(self, url):
        # type: (str) -> Page
        self._driver.get(url)
        return Page(self._driver)
