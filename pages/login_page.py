from .base_page import BasePage
from .locators import LoginPageLocators
import requests


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_user(self, username, password):
        username_form = self.browser.find_element(*LoginPageLocators.USERNAME_FORM)
        username_form.send_keys(username)
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_form.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def should_be_red_message_if_incorrect_data(self):
        assert self.is_element_present(*LoginPageLocators.RED_MESSAGE), "There isn't a failed login message," \
                                                                     " but inputs are incorrect"

    def should_not_be_red_message_if_correct_data(self):
        assert self.is_not_element_present(*LoginPageLocators.RED_MESSAGE), "There isn a failed login message," \
                                                                     " but inputs are correct"


def should_be_good_response():
    should_be_login_by_api_with_correct_data()
    should_not_be_login_by_api_with_invalid_data()
    should_be_logout_by_api()


def should_be_login_by_api_with_correct_data():
    url = "http://the-internet.herokuapp.com"
    data = {'username': "tomsmith",
           "password": "SuperSecretPassword!"
            }
    resp = requests.post(url + "/authenticate", data=data)
    assert resp.status_code == requests.codes.ok, f"Failed response, status code: {resp.status_code}"
    assert resp.text.find("class='flash success'") != -1, "Incorrect login and password"
    resp.close()


def should_not_be_login_by_api_with_invalid_data():
    url = "http://the-internet.herokuapp.com"
    data = {'username': "ghghdhdf",
            "password": "ddfbdfb"
            }
    resp = requests.post(url + "/authenticate", data=data)
    assert resp.status_code == requests.codes.ok, f"Failed response on login, status code: {resp.status_code}"
    assert resp.text.find("class='flash success'") == -1, "Incorrect login and password, but it could be logged"


def should_be_logout_by_api():
    url = "http://the-internet.herokuapp.com"
    pres = requests.get(url + "/logout")
    assert pres.status_code == requests.codes.ok, f"Failed response on logout, status code: {pres.status_code}"




