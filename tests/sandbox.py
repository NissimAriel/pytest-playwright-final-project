from playwright.sync_api import Page, Playwright
import pytest
from pytest_playwright.pytest_playwright import playwright


@pytest.fixture(scope='function')
def setup(page: Page) -> Page:
    page.goto('https://playwright.dev/python/')
    return page


def test_playwright_python_doc(playwright: Playwright, setup):
    page = setup
    page.get_by_role(role='link', name='Docs').click()
    page.wait_for_timeout(3000)
