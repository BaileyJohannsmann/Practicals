"""
CP1404 - Practical 5
state_names
a program that uses a 'constant' (name is ALL_CAPS) dictionary to store the Australian state abbreviations and names
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state")
        state = input("Enter short state: ").upper()
