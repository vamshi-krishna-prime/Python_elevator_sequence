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
    print_delay(first_count)
    print_delay(id_card)
    if first_count == 1 and id_card == "not received":
        print_delay("The clerk greets you and gives you your ID card.")
        id_card = "received"
    elif first_count > 1 and id_card == "received":
        print_delay("The clerk greets you, "
                    "but shea has already given you your ID card, "
                    "so there is nothing more to do here now.")

def choose_floor():
    print_delay("Plaese enter a number for the floor you would like to visit")
    choice= input("1. Lobby \n"
                  "2. Human resources \n"
                  "3. Engineering department \n")
    if choice == "1":
        first_floor()
    choose_floor()



first_count = 0
second_count = 0
third_count = 0
id_card = "not received"
intro()
choose_floor()
