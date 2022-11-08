def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        if not front_is_clear():
            turn_right()
            move()
        elif front_is_clear() and not right_is_clear():
            move()
        elif right_is_clear() and front_is_clear():
            if right_is_clear():
                turn_right()
                while front_is_clear():
                    move()
            elif front_is_clear():
                move()
        elif right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
    else:
        turn_left()