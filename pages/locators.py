from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    SUBMIT_BUTTON = (By.NAME, "registration_submit")
    RED_MESSAGE = (By.ID, "flash")


class SecurePageLocators():
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")
    GREEN_MESSAGE = (By.CLASS_NAME, "flash.success")



