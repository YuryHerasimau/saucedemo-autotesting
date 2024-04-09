from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


MAIN_URL = "https://www.saucedemo.com/"
INVENTORY_URL = f"{MAIN_URL}inventory.html"
INVENTORY_ITEM_URL = f"{MAIN_URL}inventory-item.html?id=4"
CART_URL = f"{MAIN_URL}cart.html"
    

# Авторизация
def test_auth_positive():
    """Авторизация используя корректные данные (standard_user, secret_sauce)"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    assert browser.current_url == INVENTORY_URL, f'Incorrect URL. Expect: {INVENTORY_URL}, Actual: {browser.current_url}'

    browser.quit()


def test_auth_negative():
    """Авторизация используя некорректные данные (user, user)"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    
    browser.find_element(By.ID, 'user-name').send_keys('user')
    browser.find_element(By.NAME, 'password').send_keys('user')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    error_fileld = browser.find_element(By.XPATH, '//h3[@data-test="error"]')

    assert browser.current_url == MAIN_URL, f'Incorrect URL. Expect: {MAIN_URL}, Actual: {browser.current_url}'
    assert error_fileld.text == 'Epic sadface: Username and password do not match any user in this service'

    browser.quit()


# Корзина
def test_add_item_to_cart_via_catalog():
    """Добавление товара в корзину через каталог"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    addToCartButton = browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    addToCartButton.click()

    cartBadgeValue = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cartBadgeValue == '1', 'Item not added to cart'

    browser.quit()


def test_delete_item_from_cart_via_cart():
    """Удаление товара из корзины через корзину"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    addToCartButton = browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    addToCartButton.click()

    cartButton = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    cartButton.click()
    assert browser.current_url == CART_URL, f'Incorrect URL. Expect: {CART_URL}, Actual: {browser.current_url}'

    cartItemIsDisplayed = browser.find_element(By.CSS_SELECTOR, '#cart_contents_container > div > div.cart_list > div.cart_item').is_displayed()
    assert cartItemIsDisplayed == True

    removeButton = browser.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    removeButton.click()

    cartBadgeValue = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cartBadgeValue == '', 'Item not deleted from cart'

    browser.quit()


def test_add_item_to_cart_from_product_card():
    """Добавление товара в корзину из карточки товара"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    itemTitle = browser.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
    itemTitle.click()  

    addToCartButton = browser.find_element(By.CSS_SELECTOR, '#add-to-cart')
    addToCartButton.click()
    
    cartBadgeValue = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cartBadgeValue == '1', 'Item not added to cart'

    browser.quit()


def test_delete_item_from_cart_via_product_card():
    """Удаление товара из корзины через карточку товара"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    itemTitle = browser.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
    itemTitle.click()  

    addToCartButton = browser.find_element(By.CSS_SELECTOR, '#add-to-cart')
    addToCartButton.click()

    cartBadgeValue = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cartBadgeValue == '1', 'Item not added to cart'

    browser.quit()


# Карточка товара
def test_navigate_to_product_card_after_clicking_on_item_image():
    """Успешный переход к карточке товара после клика на картинку товара"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    itemImage = browser.find_element(By.CSS_SELECTOR, '#item_4_img_link > img')
    itemImage.click()

    assert browser.current_url == INVENTORY_ITEM_URL, f'Incorrect URL. Expect: {INVENTORY_ITEM_URL}, Actual: {browser.current_url}'

    browser.quit()


def test_navigate_to_product_card_after_clicking_on_item_title():
    """Успешный переход к карточке товара после клика на название товара"""
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    itemTitle = browser.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
    itemTitle.click()

    assert browser.current_url == INVENTORY_ITEM_URL, f'Incorrect URL. Expect: {INVENTORY_ITEM_URL}, Actual: {browser.current_url}'

    browser.quit()