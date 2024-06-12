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
    card_contents = [
        [
            0,
            "Sauce Labs Backpack",
            "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
        ],
        [
            1,
            "Sauce Labs Bike Light",
            "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        ],
        [
            2,
            "Sauce Labs Bolt T-Shirt",
            "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
        ],
        [
            3,
            "Sauce Labs Fleece Jacket",
            "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
        ],
        [
            4,
            "Sauce Labs Onesie",
            "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
        ],
        [
            5,
            "Test.allTheThings() T-Shirt (Red)",
            "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
        ],
    ]
