from faker import Faker


def fake_first_name():
    fake = Faker()
    full_name = fake.name()
    first_name = full_name.split()[0]
    return first_name


def fake_last_name():
    fake = Faker()
    full_name = fake.name()
    last_name = full_name.split()[1]
    return last_name


def fake_zip_code():
    fake = Faker()
    return fake.postalcode()
