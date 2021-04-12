import random
import string

characters_with_special = "abcdefghijklmnopxqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+="
characters_without_special = "abcdefghijklmnopxqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def generate_password():
    password = int(input("How long would you like you password to be?"))
    special = str(input("Would like to include special characters? Y/N?"))

    if special == 'Y':
        print("Okay including special characters")
        for char in range(0, password):
            generated = random.choice(characters_with_special)
            print(generated, end="")

    elif special == 'N':
        print("special characters will not be used")
        for char in range(0, password):
            generated = random.choice(characters_without_special)
            print(generated, end="")


generate_password()