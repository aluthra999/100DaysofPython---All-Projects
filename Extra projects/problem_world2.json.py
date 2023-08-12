def turn_right():
    turn_left()
    turn_left()
    turn_left()

#while front_is_clear():
#    move()
#turn_left()
t = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        t += 1
        if t > 4:
            if front_is_clear():
                move()
            else:
                turn_left()
            t = -1
        print(t)
    elif front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
