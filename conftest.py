import random
import pytest

@pytest.fixture()
def get_name():
    name = ["Олег", "Дмитрий", "Василий", "Генадий", "Александр"]
    return name[random.randint(0,4)]

@pytest.fixture()
def get_email():
    num = random.randint(100, 999)
    email = f"oleg_shadrikov_16_{str(num)}@gmail.com"
    return email

@pytest.fixture()
def get_correctPassword():
    password = random.randint(100000, 999999)
    return str(password)

@pytest.fixture()
def get_uncorrectPasswort():
    return random.randint(1, 99999)