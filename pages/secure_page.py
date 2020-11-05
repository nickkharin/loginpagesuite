from .base_page import BasePage
from .locators import SecurePageLocators


class SecurePage(BasePage):
    def should_be_secure_page(self):
        self.should_be_secure_url()
        self.should_be_green_message()
        self.should_be_logout_button()
        self.should_be_github_link()

    def should_be_secure_url(self):
        assert "secure" in self.browser.current_url, "Incorrect secure page URL"

    def should_be_welcome_message(self):
        assert self.is_element_present(*SecurePageLocators.WELCOME_MESSAGE), "Secure page doesn't contain welcome " \
                                                                             "message"

    def should_be_logout_button(self):
        assert self.is_element_present(*SecurePageLocators.LOGOUT_BUTTON), "Secure page doesn't contain logout button"

    def should_be_log_out(self):
        button_logout = self.browser.find_element(*SecurePageLocators.LOGOUT_BUTTON)
        button_logout.click()
