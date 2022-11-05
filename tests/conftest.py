from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function')
def open_page_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.browser_name = 'chrome'
    yield

@pytest.fixture(scope='function')
def open_page_webtables():
    browser.open('https://demoqa.com/webtables')
    browser.config.browser_name = 'chrome'
    yield
