import time
items = []  # empty list to store items obtained


def print_pause(message):  # refactoring to remove repetition
    print(message)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print("Please enter the number for the floor you would like to visit:")
    floor = int(input(  # turns string to integer
        "1. Lobby\n"  # new line
        "2. Human Resources\n"
        "3. Engineering Department\n"))

    if floor == 1:
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find yourself in the lobby.")

        # if and otherwise (if have card, otherwise if not got card) => if...else structure
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already given you "
                        "your ID card, so there is nothing more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID card.")
            items.append("ID card")

    elif floor == 2:
        print_pause("You push the button for the second floor.")
        print_pause(
            "After a few moments, you find yourself in the human resources department.")

        if "handbook" in items:
            print_pause("The HR folks are busy at their desks.")
            print_pause("There doesn't seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then gives "
                            "you a copy of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't "
                            "give it to you until you go get your ID card.")

    elif floor == 3:
        print_pause("You push the button for the third floor.")
        print_pause(
            "After a few moments, you find yourself in the engineering department.")

        if "ID card" in items:
            print_pause("You use your ID card to open the door.")
            print_pause("Your program manager greets you and tells you that you need to have a copy of the "
                        "employee handbook in order to start work.")

            if "handbook" in items:
                print_pause("Fortunately, you got that from HR!")
                print_pause(
                    "Congratulatons! You are ready to start your "
                    "new job as vice president of engineering!")
                # breaks the while loop so does not ask what floor want etc.
                break

            else:
                print_pause("They scowl when they see that you don't have it, "
                            "and send you back to the elevator.")

        else:
            print_pause(
                "Unfortunately, the door is locked and you can't get in.")
            print_pause(
                "It looks like you need some kind of key card to open the door.")
            print_pause("You head back to the elevator.")

    print_pause("Where would you like to go next?")
