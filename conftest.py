import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")

from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language_page = request.config.getoption('--language')
    language = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

