import random

def get_name():
    name = ["Олег", "Дмитрий", "Василий", "Генадий", "Александр"]
    return name[random.randint(0,4)]


def get_email():
    num = random.randint(100, 999)
    email = f"{get_name()}_shadrikov_16_{str(num)}@gmail.com"
    return email


def get_correctPassword():
     password = random.randint(100000, 999999)
     return str(password)


def get_uncorrectPasswort():
    return random.randint(1, 99999)