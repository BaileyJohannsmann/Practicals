"""
CP1404 - Practical 5
hex_colours
a program that allows you to look up hexadecimal colour codes
"""

HEX_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50", "Amber": "#ffbf00",
                 "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                 "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {HEX_COLOUR.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
