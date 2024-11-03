import pytest
from playwright.sync_api import Page, expect
from pages.login_page import login_page
from utilities.test_data import test_data_for_valid_login, test_data_for_not_valid_login, base_url, after_login_url


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = login_page(page)

    @pytest.mark.parametrize("username, password", test_data_for_valid_login)
    def test_valid_login(self, page: Page, username: str, password: str) -> None:
        page.goto(base_url)
        self.login_page.login(username, password)
        expect(page).to_have_url(after_login_url, timeout=5000)

    @pytest.mark.parametrize("username, password, error_message", test_data_for_not_valid_login)
    def test_not_valid_login(self, page: Page, username: str, password: str, error_message: str) -> None:
        page.goto(base_url)
        self.login_page.login(username, password)
        error_message_element = self.login_page.get_error_message_element()
        expect(error_message_element).to_be_visible()
        expect(error_message_element).to_have_text(error_message)

