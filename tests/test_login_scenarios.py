import pytest
from playwright.sync_api import Page, expect
from pages.login_page import login_page
from utilities.test_data import test_data_for_valid_login
from utilities.test_data import test_data_for_not_valid_login



class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = login_page(page)

    @pytest.mark.parametrize("username, password", test_data_for_valid_login)
    def test_valid_login(self, page: Page, username: str, password: str) -> None:
        page.goto("https://www.saucedemo.com/")
        self.login_page.login(username, password)
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=5000)

    @pytest.mark.parametrize("username, password, error_message", test_data_for_not_valid_login)
    def test_not_valid_login(self, page: Page, username: str, password: str, error_message: str) -> None:
        page.goto("https://www.saucedemo.com/")
        self.login_page.login(username, password)
        self.login_page.validate_error_message(error_message)
















# @pytest.mark.parametrize("username, password", test_data)
# def test_valid_login_scenarios(page: Page, username: str, password: str) -> None:
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").fill(username)
#     page.locator("[data-test=\"password\"]").fill(password)
#     page.locator("[data-test=\"login-button\"]").click()
#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=5000)
#     expect(page.locator("[data-test='title']")).to_contain_text("Products")
