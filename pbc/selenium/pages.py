from pbc.selenium.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import re


class Page(BasePage):

    def __init__(self, browser):
        self._browser = browser

    def get_title(self):
        return self._browser.title

    def source(self):
        return self._browser.page_source

    def screenshot(self, name):
        self._browser.save_screenshot(name)

    def enter_data(self, input_element_name, value):
        elem = self._browser.find_element_by_name(input_element_name)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)

    def close(self):
        self._browser.close()


class ConsolePage(Page):

    def get_number_of_firefoxes(self):
        elements = self._browser.find_elements_by_xpath("//div[@type='browsers']//img[contains(@title,'firefox')]")
        return len(elements)

    def get_number_of_sessions(self):
        element = self._browser.find_element_by_xpath("//li[@type='config']/a")
        element.click()

        elements = self._browser.find_elements_by_xpath("//div[@type='config']//p")
        for element in elements:
            match = re.match(r'maxSession: (?P<count>\d+)', element.text)
            if match:
                count = match.group('count')
                return int(count)
        return 0
