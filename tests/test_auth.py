from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.data import Urls, Auth
from utils.locators import LoginForm


def test_auth_positive(driver_with_auth):
    """Авторизация используя корректные данные (standard_user, secret_sauce)"""
    assert driver_with_auth.current_url == Urls.INVENTORY_URL, f'Incorrect URL. Expected: {Urls.INVENTORY_URL}, Actual: {driver_with_auth.current_url}'


def test_auth_negative(driver):
    """Авторизация используя некорректные данные (user, user)"""
    driver.get(Urls.MAIN_URL)
    driver.find_element(By.XPATH, LoginForm.USERNAME_FIELD).send_keys(Auth.INVALID_LOGIN)
    driver.find_element(By.XPATH, LoginForm.PASSWORD_FIELD).send_keys(Auth.INVALID_PASSWORD)
    driver.find_element(By.XPATH, LoginForm.LOGIN_BUTTON).click()
    error_fileld = driver.find_element(By.XPATH, LoginForm.ERROR_MESSAGE)
    assert driver.current_url == Urls.MAIN_URL, f'Incorrect URL. Expected: {Urls.MAIN_URL}, Actual: {driver.current_url}'
    assert error_fileld.text == 'Epic sadface: Username and password do not match any user in this service', 'Incorrect error message'
