from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    url_def = "http://the-internet.herokuapp.com/login"

    def __init__(self, browser, url=url_def, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_be_github_link(self):
        assert self.is_element_present(*BasePageLocators.GITHUB_LINK), "There is no GITHUB link on page"

    def should_be_green_message(self):
        assert self.is_element_present(*BasePageLocators.GREEN_MESSAGE), "There isn't green message on page"
