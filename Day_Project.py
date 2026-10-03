# ReeBorg's maze world solve
from reeborg import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        if right_is_clear():
            turn_right()
            move()
            continue
        move()
        continue
    else:
        if right_is_clear():
            turn_right()
            move()
            continue
        else:
            turn_left()
            if front_is_clear():
                move()
                continue