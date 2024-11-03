from playwright.sync_api import Page, expect
import utilities

class login_page:
    def __init__(self, page: Page):
        self.page = page
        self.user_name_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    def login(self, username: str, password: str):

        self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def validate_error_message(self, expected_error: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_error)