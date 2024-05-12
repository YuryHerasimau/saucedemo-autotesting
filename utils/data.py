from functions.fake_data import fake_first_name, fake_last_name, fake_zip_code


class Login:
    VALID_LOGIN = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    INVALID_LOGIN = "user"
    INVALID_PASSWORD = "user"


class OrderData:
    invalid_user_data = [
        ["", fake_last_name(), fake_zip_code(), "Error: First Name is required"],
        [fake_first_name(), "", fake_zip_code(), "Error: Last Name is required"],
        [fake_first_name(), fake_last_name(), "", "Error: Postal Code is required"],
    ]

    valid_user_data = [fake_first_name(), fake_last_name(), fake_zip_code()]
    successful_message = "Thank you for your order!"


class MainData:
    header_title = "Products"

    sorting_by_price = [
        ["Price (low to high)", False, "Price not in ascending order"],
        ["Price (high to low)", True, "Price not in descending order"],
    ]

    sorting_by_name = [
        ["Name (A to Z)", False, "Price not in from A to Z order"],
        ["Name (Z to A)", True, "Price not in from Z to A order"],
    ]
