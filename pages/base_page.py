from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utils.locators import LoginFormLocators
from utils.data import Login


class BasePage:
    locators = LoginFormLocators()
    user = Login()
    timeout = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self):
        self.element_is_visible(self.locators.USERNAME_FIELD).send_keys(
            self.user.VALID_LOGIN
        )
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(
            self.user.VALID_PASSWORD
        )
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()

    def open(self):
        self.driver.get(self.url)

    def get_text(self, locator):
        # return self.driver.find_element(*locator).text
        return self.element_is_visible(locator).text

    def get_length(self, locator):
        # return len(self.driver.find_elements(*locator))
        return len(self.elements_are_visible(locator))

    def click_on_element(self, locator):
        # self.driver.find_element(*locator).click()
        self.element_is_clickable(locator).click()

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def element_is_not_present(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def element_is_displayed(self, element):
        return element.is_displayed()

    def select_by_visible_text(self, locator, value):
        product_selector = self.driver.find_element(*locator)
        select = Select(product_selector)
        select.select_by_visible_text(value)
