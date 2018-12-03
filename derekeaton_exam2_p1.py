#!/usr/bin/env python3
"""
This is Python Exam Problem 2. It will ask the
user to enter a password and then ask them to
re-enter it.
If the passwords don't match, are not at least 8 chars long,
don't have at least one uppercase and one lowercase letter,
or don't have at least one digit, the code says that the password
is invalid and reprompts the user.
"""
from __future__ import print_function


def isvalidpassword(password):
    """
    Takes password as input and tests to see if it is
    valid. (Has one or more of: uppercase, lowercase, digit)
    Args:
        password: The password being tested
    Returns:
        True if passed, False if failed
    """
    length = False
    upper = False
    lower = False
    digit = False
    if len(password) >= 8:
        length = True

    for char in password:
        if char >= "a" and char <= "z":
            lower = True
        if char >= "A" and char <= "Z":
            upper = True
        if char >= "0" and char <= "9":
            digit = True
    return length and upper and lower and digit


def main():
    """
    Test your module
    """
    running = True
    while running:
        print("Enter your password: ", end="")
        pass1 = input()
        print("Re-enter your password: ", end="")
        pass2 = input()
        if pass1 == pass2:
            if isvalidpassword(pass1):
                print("The password is valid.")
                running = False
            else:
                print("The password is invalid.")
        else:
            print("The passwords don't match.")


if __name__ == "__main__":
    main()
    exit(0)
