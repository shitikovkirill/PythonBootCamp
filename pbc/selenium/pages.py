from pbc.selenium.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import base_driver
import re
import typing


class Page(BasePage):

    def __init__(self, browser): # type: (base_driver.BaseDriver) -> None
        self._browser = browser

    def get_title(self): # type: () -> str
        return self._browser.title

    def source(self): # type: () -> str
        return self._browser.page_source

    def screenshot(self, name): # type: () -> None
        self._browser.save_screenshot(name)

    def enter_data(self, input_el_name, value, button): # type: (str, str, str) -> str
        elem = self._browser.find_element_by_name(input_el_name)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)
        button = self._browser.find_element_by_xpath(button)
        button.click()

    def close(self): # type: () -> None
        self._browser.close()


class ConsolePage(Page):

    def get_number_of_firefoxes(self): # type: () -> int
        elements = self._browser.find_elements_by_xpath("//div[@type='browsers']//img[contains(@title,'firefox')]")
        return len(elements)

    def get_number_of_sessions(self): # type: () -> int
        element = self._browser.find_element_by_xpath("//li[@type='config']/a")
        element.click()

        elements = self._browser.find_elements_by_xpath("//div[@type='config']//p")
        for element in elements:
            match = re.match(r'maxSession: (?P<count>\d+)', element.text)
            if match:
                count = match.group('count')
                return int(count)
        return 0
