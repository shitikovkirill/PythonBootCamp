from pbc.selenium.base_page import BasePage


class Page(BasePage):

    def __init__(self, browser):
        self._browser = browser

    def get_title(self):
        return self._browser.title



