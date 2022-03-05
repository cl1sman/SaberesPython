def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_obstacle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

at_goal()
while at_goal() == False: # while not at_goal():
    jump_obstacle()
    at_goal()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
