import time

def print_delay(message):
    print(message)
    time.sleep(1)

print_delay("You have just arrived at your new job!")
print_delay("You are in the elevator.")
while True:
    print_delay("Please enter the number for the floor you would like to visit:")
    floor= input("1. Lobby\n"
                "2. Human resources\n"
                "3. Engineering department\n")
    if floor == "1":
        print_delay("You push the button for the first floor.")
        print_delay("After a few moments, you find yourself in the lobby.")
    elif floor == "2":
        print_delay("You push the button for the second floor.")
        print_delay("After a few moments, you find yourself in the human resources.")
    elif floor == "3":
        print_delay("You push the button for the third floor.")
        print_delay("After a few moments, you find yourself in the engineering department.")

    print_delay("Where would you like to go next?")
