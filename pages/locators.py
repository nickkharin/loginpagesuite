from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    GITHUB_LINK = (By.XPATH, "//a[@href = 'https://github.com/tourdedave/the-internet']")
    GREEN_MESSAGE = (By.CLASS_NAME, "flash.success")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login")
    USERNAME_FORM = (By.ID, "username")
    PASSWORD_FORM = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.radius")
    RED_MESSAGE = (By.ID, "flash")


class SecurePageLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")
    WELCOME_MESSAGE = (By.XPATH, "//h4[@class = 'subheader']")
