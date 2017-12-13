import pytest
from pbc.selenium.browser import FirefoxBrowser


@pytest.mark.browser
def test_title(assert_checker):
    assert_checker.count_of_java_process(2)

    browser = FirefoxBrowser()
    browser.get_page('http://192.168.33.10:4444/grid/console')