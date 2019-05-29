# this is a sub code to test 'floor_action' funtion in 'elevator_functions_simplified.py'
import time
def print_delay(message):
    print(message)
    time.sleep(1)

complex= [["a","b","c"],
       ["d","e","f"],
       "",
       "1","2","3"]

def floor_action(list):
    for index in range(len(list)):
        for alpha in list[index]:
            print_delay(alpha)

floor_action(complex)

