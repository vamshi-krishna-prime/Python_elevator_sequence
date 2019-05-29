import time

def Intro():
    print_delay("You have just arrived at your new job!")
    print_delay("You are in the elevator.")

def print_delay(string):
    print(string)
    time.sleep(1)

def floor(number, option):
    print_delay("You push the button for the " + number + " floor.")
    print_delay("After a few movements, you find yourself in the " + option + ".")
    print_delay("Where would you like to go next?")

def choose_floor():
    print_delay("Please enter the number for the floor"
                " you would like to visit:")
    choice=input("1.Lobby\n"
                "2.Human resources\n"
                "3.Engineering department\n")
    if choice == "1":
        floor("first", "lobby")
    elif choice == "2":
        floor("second","human resources")
    elif choice == "3":
        floor("third","engineering department")
    choose_floor()

Intro()
choose_floor()
