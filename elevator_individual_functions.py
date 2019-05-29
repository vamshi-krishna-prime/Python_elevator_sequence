import time

def print_delay(message):
    print(message)
    time.sleep(1)

def intro():
    print_delay("You have just arrived at your new job!")
    print_delay("You are in the elevator.")

def floor(num, department):
    print_delay("You push the button for the " + num + "floor.")
    print_dealy("After a few movements, you find yourself in the " + department)

def first_floor():
    global first_count
    global id_card
    first_count += 1
    if id_card == "not received":
        print_delay("The clerk greets you and gives you your ID card.")
        id_card = "received"
    elif id_card == "received":
        print_delay("The clerk greets you, "
                    "but she has already given you your ID card, "
                    "so there is nothing more to do here now.")

def second_floor():
    global id_card
    global employee_handbook
    global second_count
    second_count += 1
    if id_card == "not received":
        print_delay("The head of HR greets you.")
        print_delay("He has something for you, but says he can't give it to you"
                    " untill you go get your ID card.")
    elif id_card == "received" and employee_handbook == "not received":
        print_delay("The head of HR greets you.")
        print_delay("He looks at your ID card and then "
                    "gives you a copy of the employee handbook.")
        employee_handbook = "received"
    elif id_card == "received" and employee_handbook == "received":
        print_delay("The HR folks are busy at their desks.")
        print_delay("There doesn't semm to be much to do here.")
    print_delay("You head back to the elevator.")

def third_floor():
    global id_card
    global employee_handbook
    global third_count
    third_count += 1
    print_delay("This is where you work!")
    if id_card == "not received":
        print_delay("Unfortunately, the door is locked and you can't get in.")
        print_delay("It looks like you need some kind of  "
                    "keycard to open the door.")
        print_delay("You head back to the elevator.")
    elif id_card == "received" and employee_handbook == "not received":
        print_delay("You use your ID card to open the door.")
        print_delay("Your program manager greets you and tells you that "
                    "you need to have a copy of the employee handbook "
                    "in order to start work.")
        print_delay("They scowl when they see that you don't have it, "
                    "and send you back to the elevator.")
    elif id_card == "received" and employee_handbook == "received":
        print_delay("You use your ID card to open the door.")
        print_delay("Your program manager greets you and tells you that "
                    "you need to have a copy of the employee handbook "
                    "in order to start work.")
        print_delay("Fortunately, you got that from HR!")
        print_delay("Congratulations! you are ready to start your new job "
                    "as vice president of engineering!")

def choose_floor():
    print_delay("Plaese enter a number for the floor you would like to visit")
    choice= input("1. Lobby \n"
                  "2. Human resources \n"
                  "3. Engineering department \n")
    if choice == "1":
        first_floor()
    elif choice == "2":
        second_floor()
    elif choice == "3":
        third_floor()
    else:
        print_delay("")
    choose_floor()


first_count = 0
second_count = 0
third_count = 0
id_card = "not received"
employee_handbook = "not received"
intro()
choose_floor()
