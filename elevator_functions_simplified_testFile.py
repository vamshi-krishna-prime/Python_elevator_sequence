# this is a sub code to test 'floor_action' funtion in 'elevator_functions_simplified.py'
import time
def print_delay(message):
    print(message)
    time.sleep(1)

complex= ["a","b","","","c"]

def floor_action(list):
    for alpha in list:
        print_delay(alpha)

floor_action(complex)
