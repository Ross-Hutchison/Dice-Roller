import re
import roll_handler

diceType = "unassigned"
diceCount = "unassigned"
inputType = "unassigned"
manyDiceInput = "unassigned"
manyDicePluses = "unassigned"


def decide_input():
    global inputType
    while not bool(re.search("^[yn]$", inputType)):
        inputType = "undefined"
        inputType = input("Do you want to roll multiple types of dice e.g 4d4 and 3d10 (y/n)\n")

    if inputType == "y":
        set_input_many()
    elif inputType == "n":
        set_input_single()


def set_input_single():
    global diceType
    global diceCount
    global inputType

    diceType_input = "unassigned"
    diceCount_input = "unassigned"
    inputType = "single"

    while not bool(re.search("^\d*$", diceType_input)):
        diceType_input = input("enter the dice type as an integer value e.g 6 for standard dice 12 for d12 etc\n")

    while not bool(re.search("^\d*$", diceCount_input)):
        diceCount_input = input("enter the number of dice to roll\n")

    diceType = int(diceType_input)
    diceCount = int(diceCount_input)


def set_input_many():
    global manyDiceInput
    global manyDicePluses
    global inputType

    inputType = "many"
    while not bool(re.search("^(\d+d\d+)(( \d+d\d+| \+\d)*)$", manyDiceInput)):
        manyDiceInput = input("enter the number of dice you want to roll usage: <xdy>1 ... <xdy>n\n")

    dice_list = re.findall("(\d+d\d+)", manyDiceInput)
    bonuses_list = re.findall("\+\d", manyDiceInput)
    manyDiceInput = dice_list
    manyDicePluses = bonuses_list


def handle_input():
    global diceType
    global diceCount
    global inputType
    global manyDiceInput

    if inputType == "unassigned":
        print("an error occurred: the input type has not been assigned yet\n")
        exit(1)

    elif inputType == "single":
        print("\nrolling")
        return roll_handler.roll(diceCount, diceType)

    elif inputType == "many":
        total = 0
        for x in manyDiceInput:
            parts = x.split("d")
            print("\nrolling d" + parts[1] + "s")
            total += roll_handler.roll(int(parts[0]), int(parts[1]))

        print("\nadding bonuses")
        for x in manyDicePluses:
            print(x)
            parts = x.split("+")
            total += int(parts[1])

        diceType = "unassigned"
        diceCount = "unassigned"
        inputType = "unassigned"
        manyDiceInput = "unassigned"
        return total


def get_dice_type():
    return diceType


def get_dice_count():
    return diceCount



