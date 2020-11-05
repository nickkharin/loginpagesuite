from .base_page import BasePage
from .locators import LoginPageLocators


class SecurePage(BasePage):
    def should_be_secure_page(self):
        self.should_be_secure_url()
        self.should_be_green_message()

    def should_be_secure_url(self):
        assert "secure" in self.browser.current_url, "Incorrect login URL"

    def should_be_green_message(self):
        assert self.is_element_present('*SecurePageLocators.GREEN_MESSAGE'), "There isn't a successful login message," \
                                                                              " but inputs are incorrect"

    def should_be_logout_button(self):
        assert self.is_element_present('*SecurePageLocators.LOGOUT_BUTTON'), "Secure pages doesn't contain logout button"
