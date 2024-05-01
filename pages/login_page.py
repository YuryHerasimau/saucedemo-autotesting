from pages.base_page import BasePage
from utils.locators import LoginFormLocators
from utils.data import Login


class LoginPage(BasePage):
    locators = LoginFormLocators()
    user = Login()

    # def login(self):
    #     self.driver.find_element(*self.locators.USERNAME_FIELD).send_keys(self.user.VALID_LOGIN)
    #     self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(self.user.VALID_PASSWORD)
    #     self.driver.find_element(*self.locators.LOGIN_BUTTON).click()
