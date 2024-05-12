from pages.base_page import BasePage
from utils.locators import LoginFormLocators
from utils.data import Login


class LoginPage(BasePage):
    locators = LoginFormLocators()
    user = Login()
