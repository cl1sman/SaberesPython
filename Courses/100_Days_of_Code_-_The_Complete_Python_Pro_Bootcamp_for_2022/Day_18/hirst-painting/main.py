from turtle import Screen, Turtle
import random
import turtle

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 110), (239, 245, 241), (150, 75, 50), (221, 201, 136), (53, 93, 126), (126, 28, 20), (184, 158, 46), (53, 110, 57), (172, 28, 33), (57, 46, 43), (215, 128, 147), (141, 184, 161), (238, 176, 165), (44, 60, 68), (26, 96, 71), (86, 31, 35), (133, 163, 183), (177, 200, 216), (239, 171, 177), (26, 56, 48), (156, 21, 18), (46, 49, 54), (231, 161, 154), (21, 66, 56), (232, 164, 168), (21, 74, 83), (160, 29, 25), (21, 80, 69), (231, 165, 161), (160, 189, 202), (65, 44, 40), (17, 90, 76), (22, 83, 89), (173, 192, 179), (94, 123, 140), (16, 85, 84), (101, 127, 148), (174, 205, 193), (16, 87, 80), (99, 140, 125), (16, 93, 86), (16, 78, 77), (16, 92, 91), (16, 82, 87), (16, 84, 90), (16, 91, 85), (16, 89, 88), (16, 90, 93), (16, 88, 92), (16, 91, 89), (16, 89, 90), (16, 90, 91), (16, 91, 90), (16, 90, 90), (16, 90, 91), (16, 90, 45)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0) # start drawing from the left
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()