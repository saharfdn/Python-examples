import string


def check_letter(password):
    for i in password:
        if i in string.ascii_letters:
            return True
    else:
        return False


def check_digit(password):
    for i in password:
        if i in string.digits:
            return True

    else:
        return False


def check_uppercase_letter(password):
    for i in password:
        if i in string.ascii_uppercase:
            return True
    else:
        return False


def check_special_characters(password):
    for i in password:
        if i in string.punctuation:
            return True
    else:
        return False


def check_pass(password):
    if len(password) >= 6 and len(password) <= 12:
        if check_letter(password) and check_digit(password) and check_special_characters(
                password) and check_uppercase_letter(password):
            return True
    else:
        return False


passwords = input("enter passwords: ")
passwords = passwords.split(',')
for i in passwords:
    if check_pass(i):
        print(i, end=' ')


