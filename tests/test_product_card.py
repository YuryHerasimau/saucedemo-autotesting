from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.data import Urls, Auth
from utils.locators import LoginForm, Inventory


def test_navigate_to_product_card_by_clicking_on_item_image(driver_with_auth):
    """Успешный переход к карточке товара после клика на картинку товара"""
    itemImage = driver_with_auth.find_element(By.CSS_SELECTOR, Inventory.ITEM_IMAGE)
    itemImage.click()
    assert driver_with_auth.current_url == Urls.INVENTORY_ITEM_URL, f'Incorrect URL. Expected: {Urls.INVENTORY_ITEM_URL}, Actual: {driver_with_auth.current_url}'


def test_navigate_to_product_card_by_clicking_on_item_title(driver_with_auth):
    """Успешный переход к карточке товара после клика на название товара"""
    itemTitle = driver_with_auth.find_element(By.CSS_SELECTOR, Inventory.ITEM_NAME)
    itemTitle.click()
    assert driver_with_auth.current_url == Urls.INVENTORY_ITEM_URL, f'Incorrect URL. Expected: {Urls.INVENTORY_ITEM_URL}, Actual: {driver_with_auth.current_url}'
    