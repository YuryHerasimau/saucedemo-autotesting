class LoginForm:
    USERNAME_FIELD = '//input[@data-test="username"]'
    PASSWORD_FIELD = '//input[@data-test="password"]'
    LOGIN_BUTTON = '//input[@data-test="login-button"]'
    ERROR_MESSAGE = '//h3[@data-test="error"]'


class Inventory:
    ITEM_IMAGE = '#item_4_img_link > img'
    ITEM_NAME = '#item_4_title_link > div'
    ADD_TO_CART_BUTTON = '#add-to-cart-sauce-labs-backpack'


class InventoryItem:
    ADD_TO_CART_BUTTON = '#add-to-cart'
    REMOVE_BUTTON = '#remove'


class Cart:
    CART_TITLE = '//*[@id="header_container"]/div[2]/span'
    ITEM_NAME = '#item_4_title_link > div'
    ITEM_PRICE = "(//div[@class='inventory_item_price'])[1]"
    ITEM_QTY = "(//div[@class='cart_quantity'])[1]"
    REMOVE_ITEM_BUTTON = "(//div[@class='item_pricebar']/button)[1]"


class Header:
    CART_BADGE = '#shopping_cart_container > a'


class Footer:
    pass


class Sidebar:
    pass