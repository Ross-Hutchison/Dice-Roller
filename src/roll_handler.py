import random

def roll(diceCount, diceType):
    total = 0
    for x in range(diceCount):
        current_roll = random.randrange(1, diceType)
        total += current_roll
        print(str(current_roll))

    return total