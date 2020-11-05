import allure
from allure_commons.types import AttachmentType
from .pages.login_page import LoginPage
from .pages.login_page import should_be_good_response
from .pages.secure_page import SecurePage


class TestLoginPage:
    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Login page content')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step
    @allure.description('This test verifies that the guest can open the login page and '
                        'that it contains all the necessary elements')
    def test_guest_can_open_login(self, browser):
        page = LoginPage(browser)
        page.open()
        with allure.step('Taking a screenshot of the login page content:'):
            allure.attach(browser.get_screenshot_as_png(), name='Content_LPage_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_login_page()

    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Log in')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step
    @allure.description('This test verifies that the guest can successfully login with correct data')
    def test_guest_can_login(self, browser):
        page = LoginPage(browser)
        page.open()
        page.should_be_user_login_in()
        with allure.step('Taking a screenshot of the successful log in:'):
            allure.attach(browser.get_screenshot_as_png(), name='Successful_SPage_screenshot',
                          attachment_type=AttachmentType.PNG)

    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Red alert')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    @allure.description('This test verifies that the guest will not be able to successfully '
                        'login with invalid data and will see a red error message')
    def test_guest_can_see_message_if_input_wrong(self, browser):
        username = 'gtomsmithf'
        page = LoginPage(browser)
        page.open()
        page.should_be_user_login_in(username)
        with allure.step('Taking a screenshot of the login page with incorrect input:'):
            allure.attach(browser.get_screenshot_as_png(), name='Incorrect_LPage_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_red_message()

    @allure.epic('UI Tests')
    @allure.story('Login page')
    @allure.feature('Private access')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    @allure.description('This test verifies that an unauthorized guest will see an error message '
                        'when trying to access a secure page.')
    def test_guest_can_not_open_secure_page(self, browser):
        link = 'http://the-internet.herokuapp.com/secure'
        page = LoginPage(browser, link)
        page.open()
        with allure.step('Taking a screenshot of the login page:'):
            allure.attach(browser.get_screenshot_as_png(), name='NoAccess_SPage_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_red_message()


class TestSecurePage:
    @allure.epic('UI Tests')
    @allure.story('Secure page')
    @allure.feature('Log in')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    @allure.description('This test verifies that the user can see the secure page after a successful login '
                        'and that the secure page contains all the necessary elements')
    def test_user_can_open_secure_page(self, browser):
        page = LoginPage(browser)
        page.open()
        page.should_be_user_login_in()
        secure_page = SecurePage(browser, browser.current_url)
        with allure.step('Taking a screenshot of the login page after log out:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_SPage_screenshot',
                          attachment_type=AttachmentType.PNG)
        secure_page.should_be_secure_page()

    @allure.epic('UI Tests')
    @allure.story('Secure page')
    @allure.feature('Log out')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    @allure.description('This test verifies that the user can log out by clicking on the button and '
                        'can see a successful logout message')
    def test_user_can_logout(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.should_be_user_login_in()
        secure_page = SecurePage(browser, browser.current_url)
        secure_page.should_be_log_out()
        with allure.step('Taking a screenshot of the login page after log out:'):
            allure.attach(browser.get_screenshot_as_png(), name='LOut_LPage_screenshot',
                          attachment_type=AttachmentType.PNG)
        login_page.should_be_green_message()


@allure.epic('API Tests')
@allure.severity(allure.severity_level.BLOCKER)
@allure.step
@allure.description('This test verifies log in and log out actions by API')
def test_correct_responses():
    should_be_good_response()
