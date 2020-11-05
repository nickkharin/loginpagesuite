from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_form.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def should_be_red_message_if_incorrect_data(self):
        assert self.is_not_element_present('*LoginPageLocators.RED_MESSAGE'), "There isn't a failed login message," \
                                                                     " but inputs are incorrect"

    def should_not_be_red_message_if_correct_data(self):
        assert self.is_element_present('*LoginPageLocators.RED_MESSAGE'), "There isn a failed login message," \
                                                                     " but inputs are correct"




