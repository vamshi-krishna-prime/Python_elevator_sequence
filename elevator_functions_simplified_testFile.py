# this is a sub code to test 'floor_action' funtion in 'elevator_functions_simplified.py'
import time
def print_delay(message):
    print(message)
    time.sleep(1)

list1= [["a","b","c"],
       ["d","e","f"],
       "",
       ""]

list2= [["a"],
       ["b"],
       ["c"],
       ["d"]]

list3= [["e"],
       ["f"],
       ["g"],
       ["h"]]


def floor_action(list, extra):
    test= int(input("enter a number:"))
    if test == 1:
        for index in list[0]:
            print_delay(index)
    elif test == 2:
        print_delay(list[1])
        if extra == "no":
            print_delay(list[2])
        elif extra == "yes":
            print_delay(list[3])

floor_action(list1, "no")
