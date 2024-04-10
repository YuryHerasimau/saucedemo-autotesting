class Urls:
    MAIN_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = f"{MAIN_URL}inventory.html"
    INVENTORY_ITEM_URL = f"{MAIN_URL}inventory-item.html?id=4"
    CART_URL = f"{MAIN_URL}cart.html"


class Auth:
    VALID_LOGIN = 'standard_user'
    VALID_PASSWORD = 'secret_sauce'
    INVALID_LOGIN = 'user'
    INVALID_PASSWORD = 'user'