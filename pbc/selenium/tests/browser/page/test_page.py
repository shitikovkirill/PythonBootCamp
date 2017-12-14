import pytest
import re
import time

from pbc.selenium.pages import ConsolePage
import requests


@pytest.mark.page
def test_page(web_driver, assert_checker):
    assert_checker.count_of_java_process(2)

    web_driver.get("http://192.168.33.10:4444/grid/console")
    page = ConsolePage(web_driver)
    number_of_firefoxes = page.get_number_of_firefoxes()
    number_of_sessions = page.get_number_of_sessions()

    assert number_of_firefoxes == 5
    assert number_of_sessions == 4


@pytest.mark.firefox_image
def test_check_firefox_image_using_requests(assert_checker):
    assert_checker.count_of_java_process(2)

    request = requests.get('http://192.168.33.10:4444/grid/console')

    count = request.text.count("src='/grid/resources/org/openqa/grid/images/firefox.png'")
    assert count == 5


@pytest.mark.max_session
def test_check_max_session_using_requests(assert_checker):
    assert_checker.count_of_java_process(2)

    request = requests.get('http://192.168.33.10:4444/grid/console')

    match = re.search(r'maxSession: (?P<count>\d+)', request.text)
    if match:
        count = match.group('count')
        assert int(count) == 5
    else:
        raise Exception('maxSession do not find')
