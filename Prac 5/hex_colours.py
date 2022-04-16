COLORS_TO_CODE = {"Amber": "#ffbf00", "Aqua": "#00ffff", "Black": "#000000", "Blond": "#faf0be",
                  "Bubble Gum": "#ffc1cc", "Candy Pink": "#e4717a", "Corn": "#fbec5d", "Orchid": "#da70d6",
                  "Blue": "0000ff", "Green": "#1cac78"}

color = input("Enter a color: ").title()
while color != "":
    if color in COLORS_TO_CODE:
        print("The Hex Code of {} is {}".format(color, COLORS_TO_CODE[color]))
    else:
        print("The Hex Code for {} is not in the dictionary.".format(color))
    color = input("Enter a color: ").title()

