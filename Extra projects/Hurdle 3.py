def turn_right():
    turn_left()
    turn_left()
    turn_left()

def way():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def tackel():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        tackel()
    else:
        way()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
