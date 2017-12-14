import pytest
import time
from pbc.selenium.browser import FirefoxBrowser


@pytest.mark.browser
def test_title(assert_checker):
    assert_checker.count_of_java_process(2)

    browser = FirefoxBrowser()
    try:
        page = browser.get_page('http://www.python.org')
        page.screenshot('python.png')
        assert "Python" in page.get_title()
        page.enter_data("q", "pycon", "//button[@id='submit']")
        time.sleep(5)
        page.screenshot('pycon.png')

        new_page = browser.get_page("http://www.python.org")
        assert "No results found." not in new_page.source()
    except Exception as a:
        print a.message
        raise a
    finally:
        print 'close'
        page.close()
