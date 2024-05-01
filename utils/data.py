class Urls:
    BASE_URL = "https://www.saucedemo.com/"
    MAIN_URL = f"{BASE_URL}inventory.html"


class Login:
    VALID_LOGIN = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    INVALID_LOGIN = "user"
    INVALID_PASSWORD = "user"


class OrderData:
    invalid_user_data = [
        ["", "Ivanov", "123456", "Error: First Name is required"],
        ["Denis", "", "123456", "Error: Last Name is required"],
        ["Denis", "Ivanov", "", "Error: Postal Code is required"],
    ]

    valid_user_data = ["Denis", "Ivanov", "123456"]
    successful_message = "Thank you for your order!"


class MainData:
    sorting_by_price = [
        ["Price (low to high)", False, "Price not in ascending order"],
        ["Price (high to low)", True, "Price not in descending order"],
    ]
    
    sorting_by_name = []
