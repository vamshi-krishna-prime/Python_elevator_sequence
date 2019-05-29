import time

def print_delay(message):
    print(message)
    time.sleep(1)

def intro():
    print_delay("You have just arrived at your new job!")
    print_delay("You are in the elevator.")

def floor_message(num, department):
    print_delay("You push the button for the " + num + "floor.")
    print_delay("After a few movements, you find yourself in the " + department)

def floor_action(floor, list):
    global id_card
    global employee_handbook
    if id_card == "not received":
        for message in list[0]:
            print_delay(message)
        if floor == "first":
            id_card = "received"
    elif id_card == "received":
        if floor == "first" or floor == "third":
            for message in list[1]:
                print_delay(message)
        if employee_handbook == "not received":
            if floor == "first":
                return "not required"
            for message in list[2]:
                print_delay(message)
            if floor == "second":
                employee_handbook = "received"
        elif employee_handbook == "received":
            if floor == "first":
                return "not required"
            for message in list[3]:
                print_delay(message)
            if floor == "third":
                return "end"

def choose_floor():
    print_delay("Plaese enter a number for the floor you would like to visit")
    choice= input("1. Lobby \n"
                  "2. Human resources \n"
                  "3. Engineering department \n")
    if choice == "1":
        floor_message("first", "lobby")
        floor_action("first", list1)
    elif choice == "2":
        floor_message("second", "human resources")
        floor_action("second", list2)
    elif choice == "3":
        floor_message("third", "engineering department")
        # third_floor() -no need to use, below line runs function as well assign
        terminate = floor_action("third", list3)
        if terminate == "end":
            return "program terminated"
    else:
        print_delay("")
    choose_floor()

list1= [["The clerk greets you and gives you your ID card."],
        ["The clerk greets you, but she has already given you your ID card, "
         "so there is nothing more to do here now."],
         "",
         ""]

list2= [["The head of HR greets you.", "He has something for you, but says he "
         "can't give it to you untill you go get your ID card.",
         "You head back to the elevator."],
        [""],
        ["The head of HR greets you.",
         "He looks at your ID card and then "
         "gives you a copy of the employee handbook.",
         "You head back to the elevator."],
        ["The HR folks are busy at their desks.",
         "There doesn't seem to be much to do here.",
         "You head back to the elevator."]]

list3= [["This is where you work!",
         "Unfortunately, the door is locked and you can't get in.",
         "It looks like you need some kind of keycard to open the door.",
         "You head back to the elevator."],
        ["This is where you work!",
         "You use your ID card to open the door.",
         "Your program manager greets you and tells you that you need to have "
         "a copy of the employee handbook in order to start work."],
        ["They scowl when they see that you don't have it, "
         "and send you back to the elevator."],
        ["Fortunately, you got that from HR!",
         "Congratulations! you are ready to start your new job "
         "as vice president of engineering!"]]

id_card = "not received"
employee_handbook = "not received"
intro()
choose_floor()
