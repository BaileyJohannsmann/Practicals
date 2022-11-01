"""
CP1404 - Practical 5
emails
a program that stores users' emails (unique keys) and names (values) in a dictionary
"""


def main():

    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (y/n) ")
        if confirmation.upper() != "y" and confirmation != "y":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print(f"{name} ({email})")


def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
