from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.data import Urls, Auth
from utils.locators import LoginForm


@pytest.fixture()
def driver():
    print('\nstart browser...')
    driver = webdriver.Chrome()
    yield driver 
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def driver_with_auth():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_URL)
    driver.find_element(By.XPATH, LoginForm.USERNAME_FIELD).send_keys(Auth.VALID_LOGIN)
    driver.find_element(By.XPATH, LoginForm.PASSWORD_FIELD).send_keys(Auth.VALID_PASSWORD)
    driver.find_element(By.XPATH, LoginForm.LOGIN_BUTTON).click()
    driver.implicitly_wait(1)
    yield driver
    driver.quit()
