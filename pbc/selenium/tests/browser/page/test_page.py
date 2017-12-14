import pytest
from pbc.selenium.pages import ConsolePage


@pytest.mark.page
def test_page(web_driver, assert_checker):
    assert_checker.count_of_java_process(2)
    web_driver.get("http://192.168.33.10:4444/grid/console")
    page = ConsolePage(web_driver)
    number_of_firefoxes = page.get_number_of_firefoxes()
    number_of_sessions = page.get_number_of_sessions()

    assert number_of_firefoxes == number_of_sessions
