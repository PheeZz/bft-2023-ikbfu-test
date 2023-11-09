import pytest
from playwright._impl._api_types import Error
from playwright.sync_api import sync_playwright

from source.configuration import config


class TestStackOverflow:
    def test_login(self) -> None:
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://stackoverflow.com/users/login")
            page.fill(
                "#email",
                config.stackoverflow_login,
            )
            page.fill(
                "#password",
                config.stackoverflow_password,
            )
            page.click("#submit-button")
            with pytest.raises(Error):
                page.wait_for_selector(
                    ".my-profile",
                    timeout=10000,
                )
            browser.close()

    def test_login_with_wrong_password(self) -> None:
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://stackoverflow.com/users/login")
            page.fill(
                "#email",
                config.stackoverflow_login,
            )
            page.fill(
                "#password",
                "wrong_password",
            )
            page.click("#submit-button")
            page.wait_for_selector(
                ".js-error-message",
                timeout=10000,
            )
            browser.close()

    def test_login_with_wrong_email(self) -> None:
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://stackoverflow.com/users/login")
            page.fill(
                "#email",
                "wrong_email",
            )
            page.fill(
                "#password",
                config.stackoverflow_password,
            )
            page.click("#submit-button")
            page.wait_for_selector(
                ".js-error-message",
                timeout=10000,
            )
            browser.close()

    def test_search(self) -> None:
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://stackoverflow.com/")
            page.fill(
                "#search > div > input",
                "python",
            )
            # click enter
            page.press(
                "#search > div > input",
                "Enter",
            )
            # wait for element with text "Ask Question"
            page.wait_for_selector(
                "text=Ask Question",
                timeout=10000,
            )
            browser.close()

    def test_signup_button(self) -> None:
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://stackoverflow.com/")
            page.click(
                ".ml4",
            )
            page.wait_for_selector(
                "#submit-button",
                timeout=10000,
            )
            browser.close()
