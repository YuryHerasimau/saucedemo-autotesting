from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.data import Urls, Auth
from utils.locators import LoginForm, Inventory, InventoryItem, Header, Cart
from tests.test_product_card import test_navigate_to_product_card_by_clicking_on_item_title


def test_add_item_to_cart_via_catalog(driver_with_auth):
    """Добавление товара в корзину через каталог"""
    addToCartButton = driver_with_auth.find_element(By.CSS_SELECTOR, Inventory.ADD_TO_CART_BUTTON)
    addToCartButton.click()
    cartBadgeValue = driver_with_auth.find_element(By.CSS_SELECTOR, Header.CART_BADGE).text
    assert cartBadgeValue == '1', f'Item not added to cart. Expected: 1, Actual: {cartBadgeValue}'


def test_delete_item_from_cart_via_cart(driver_with_auth):
    """Удаление товара из корзины через корзину"""
    test_check_item_added_to_cart(driver_with_auth)
    removeButton = driver_with_auth.find_element(By.XPATH, Cart.REMOVE_ITEM_BUTTON)
    removeButton.click()
    cartBadgeValue = driver_with_auth.find_element(By.CSS_SELECTOR, Header.CART_BADGE).text
    assert cartBadgeValue == '', 'Item was not removed from the cart'


def test_add_item_to_cart_from_product_card(driver_with_auth):
    """Добавление товара в корзину из карточки товара"""
    test_navigate_to_product_card_by_clicking_on_item_title(driver_with_auth)
    addToCartButton = driver_with_auth.find_element(By.CSS_SELECTOR, InventoryItem.ADD_TO_CART_BUTTON)
    assert addToCartButton.text == 'Add to cart', f'Text on the button does not match. Expected: Add to cart, Actual: {addToCartButton.text}'
    addToCartButton.click()
    cartBadgeValue = driver_with_auth.find_element(By.CSS_SELECTOR, Header.CART_BADGE).text
    assert cartBadgeValue == '1', 'Item not added to cart'


def test_delete_item_from_cart_via_product_card(driver_with_auth):
    """Удаление товара из корзины через карточку товара"""
    test_add_item_to_cart_from_product_card(driver_with_auth)
    removeButton = driver_with_auth.find_element(By.CSS_SELECTOR, InventoryItem.REMOVE_BUTTON)
    assert removeButton.text == 'Remove', f'Text on the button does not match. Expected: Remove, Actual: {removeButton.text}'
    removeButton.click()
    cartBadgeValue = driver_with_auth.find_element(By.CSS_SELECTOR, Header.CART_BADGE).text
    assert cartBadgeValue == '', 'Item was not removed from the cart'


def test_navigate_to_cart(driver_with_auth):
    cartButton = driver_with_auth.find_element(By.CSS_SELECTOR, Header.CART_BADGE)
    cartButton.click()
    assert driver_with_auth.current_url == Urls.CART_URL, f'Incorrect URL. Expected: {Urls.CART_URL}, Actual: {driver_with_auth.current_url}'
    cartTitle = driver_with_auth.find_element(By.XPATH, Cart.CART_TITLE).text
    assert cartTitle == 'Your Cart', f'Incorrect cart title. Expected: your cart, Actual: {cartTitle}'


def test_check_item_added_to_cart(driver_with_auth):
    test_add_item_to_cart_via_catalog(driver_with_auth)
    test_navigate_to_cart(driver_with_auth)
    itemTitle = driver_with_auth.find_element(By.CSS_SELECTOR, Cart.ITEM_NAME).text
    itemPrice = driver_with_auth.find_element(By.XPATH, Cart.ITEM_PRICE).text
    itemQty = driver_with_auth.find_element(By.XPATH, Cart.ITEM_QTY).text
    assert itemTitle == 'Sauce Labs Backpack', f'Incorrect item name. Expected: Sauce Labs Backpack, Actual: {itemTitle}'
    assert itemPrice == '$29.99', f'Incorrect item price. Expected: Sauce Labs Backpack, Actual: {itemPrice}'
    assert itemQty == '1', f'Incorrect item price. Expected: 1, Actual: {itemQty}'
