class LoginFormLocators:
    USERNAME_FIELD = ("xpath", '//input[@data-test="username"]')
    PASSWORD_FIELD = ("xpath", '//input[@data-test="password"]')
    LOGIN_BUTTON = ("xpath", '//input[@data-test="login-button"]')
    ERROR_MESSAGE = ("xpath", '//h3[@data-test="error"]')
    LOGIN_FORM = ("css selector", 'div[data-test="login-container"]')


class MainLocators:
    TITLE = ("css selector", "span[data-test='title']")
    CARDS = ("css selector", "div[data-test='inventory-item']")
    SAUCE_LABS_BACKPACK = (
        "css selector",
        "button[data-test='add-to-cart-sauce-labs-backpack']",
    )
    REMOVE_SAUCE_LABS_BACKPACK = (
        "css selector",
        "button[data-test='remove-sauce-labs-backpack']",
    )
    # CART_BUTTON = ("css selector", "a[data-test='shopping-cart-link']") # to remove!
    COUNT_ITEMS = ("css selector", "span[data-test='shopping-cart-badge']")
    BURGER_MENU_BUTTON = ("css selector", "div[class='bm-burger-button']")
    ABOUT_BUTTON = ("css selector", "a[data-test='about-sidebar-link']")
    LOGOUT_BUTTON = ("css selector", "a[data-test='logout-sidebar-link']")
    RESET_APP_STATE_BUTTON = ("css selector", "a[data-test='reset-sidebar-link']")
    PRODUCT_SELECTOR = ("css selector", "select[data-test='product-sort-container']")
    PRICE_VALUE = ("css selector", "div[data-test='inventory-item-price']")
    PRODUCT_NAME = ("css selector", "div[data-test='inventory-item-name']")


class CartLocators:
    CART_TITLE = ("xpath", '//*[@id="header_container"]/div[2]/span')
    ITEM_NAME = ("css selector", "#item_4_title_link > div")
    ITEM_PRICE = ("xpath", "(//div[@class='inventory_item_price'])[1]")
    ITEM_QTY = ("xpath", "(//div[@class='cart_quantity'])[1]")
    REMOVE_ITEM_BUTTON = ("xpath", "(//div[@class='item_pricebar']/button)[1]")
    CHECKOUT_BUTTON = ("css selector", "button[data-test='checkout']")


class OrderLocators:
    FIRST_NAME_FIELD = ("css selector", "input[data-test='firstName']")
    LAST_NAME_FIELD = ("css selector", "input[data-test='lastName']")
    ZIP_CODE_FIELD = ("css selector", "input[data-test='postalCode']")
    CONTINUE_BUTTON = ("css selector", "input[id='continue']")
    FINISH_BUTTON = ("css selector", "button[id='finish']")
    SUCCESSFULL_ORDER = ("css selector", "h2[data-test='complete-header']")
    ERROR_MESSAGE = ("css selector", "h3[data-test='error']")
