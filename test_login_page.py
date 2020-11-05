import allure
from allure_commons.types import AttachmentType
from .pages.login_page import LoginPage
from .pages.login_page import should_be_good_response
from .pages.secure_page import SecurePage


class TestLoginPage:
    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Log in')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step
    def test_guest_can_open_login(self, browser):
        page = LoginPage(browser)
        page.open()
        with allure.step('Делаем скриншот страницы страницы логина:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_LP_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_login_page()

    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Log in')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step
    def test_guest_can_login(self, browser):
        page = LoginPage(browser)
        page.open()
        page.should_be_user_login_in()

    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Red alert')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    def test_guest_can_see_message_if_input_wrong(self, browser):
        username = 'gtomsmithf'
        page = LoginPage(browser)
        page.open()
        page.should_be_user_login_in(username)
        with allure.step('Делаем скриншот страницы страницы логина некорректными данными:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_Incorrect_Login_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_red_message()


@allure.epic('API Tests')
@allure.severity(allure.severity_level.BLOCKER)
@allure.step
def test_correct_responses():
    should_be_good_response()


class TestSecurePage:
    @allure.epic('UI Tests')
    @allure.story('Secure page')
    @allure.feature('Log in')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    def test_user_can_open_secure_page(self, browser):
        page = LoginPage(browser)
        page.open()
        with allure.step('Делаем скриншот страницы страницы логина:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_LP_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_user_login_in()
        secure_page = SecurePage(browser, browser.current_url)
        secure_page.should_be_secure_page()

    @allure.epic('UI Tests')
    @allure.story('Secure page')
    @allure.feature('Log out')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    def test_user_can_logout(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        with allure.step('Делаем скриншот страницы страницы логина:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_LP_screenshot',
                          attachment_type=AttachmentType.PNG)
        login_page.should_be_user_login_in()
        secure_page = SecurePage(browser, browser.current_url)
        secure_page.should_be_log_out()
        login_page.should_be_green_message()
