import allure
from allure_commons.types import AttachmentType
from .pages.login_page import LoginPage
from .pages.login_page import should_be_good_response


class TestLoginPage():
    @allure.epic('UI Tests')
    @allure.story('Login pages')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step
    def test_guest_can_open_login(self, browser):
        link = "http://the-internet.herokuapp.com/login"
        page = LoginPage(browser, link)
        page.open()
        with allure.step('Делаем скриншот страницы страницы логина:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_LP_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_login_page()

    @allure.epic('UI Tests')
    @allure.story('Login pages')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step
    def test_guest_can_login(self, browser):
        username = 'tomsmith'
        password = 'SuperSecretPassword!'
        link = "http://the-internet.herokuapp.com/login"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_user(username, password)

    @allure.epic('UI Tests')
    @allure.story('Login pages')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step
    def test_guest_can_see_message_if_input_wrong(self, browser):
        email = 'gtomsmithf'
        password = 'gSuperSecretPassword!'
        link = "http://the-internet.herokuapp.com/login"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_user(email, password)
        with allure.step('Делаем скриншот страницы страницы логина некорректными данными:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_Incorrect_Login_screenshot',
                          attachment_type=AttachmentType.PNG)
        page.should_be_red_message_if_incorrect_data()


@allure.epic('API Tests')
@allure.severity(allure.severity_level.BLOCKER)
@allure.step
def test_be_correct_responses():
    should_be_good_response()

'''
class TestSecurePage():
    def test_user_can_open_secure_page(self, browser):
        link = "http://the-internet.herokuapp.com/login"
        pages = LoginPage(browser, link)
        pages.open()
        with allure.step('Делаем скриншот страницы страницы логина:'):
            allure.attach(browser.get_screenshot_as_png(), name='Open_LP_screenshot',
                          attachment_type=AttachmentType.PNG)
        pages.should_be_login_page()
        pages.should_be_secure_page()
'''
