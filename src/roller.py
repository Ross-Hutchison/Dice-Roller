import input_handler

import re

if __name__ == "__main__":

    terminate = False   # boolean used to  end the while loop

    while not terminate:    # loops until it is told to terminate

        # uses user input to decide if one type of dice or more are being used and takes
        # the types and amounts plus any bonuses
        # then handles those to generate a total
        input_handler.decide_input()
        total = input_handler.handle_input()

        print("\nresult: " + str(total))    # outputs the total

        # determines if the program should continue looping
        choice = input("roll again? y/n\n")
        while not bool(re.search("^[yn]$", choice)):
            choice = input("roll again? y/n\n")

        if choice == "n":
            terminate = True
        else:
            terminate = False

print("thank you for using me")

