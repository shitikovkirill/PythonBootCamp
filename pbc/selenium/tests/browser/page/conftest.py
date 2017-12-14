import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def web_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()
