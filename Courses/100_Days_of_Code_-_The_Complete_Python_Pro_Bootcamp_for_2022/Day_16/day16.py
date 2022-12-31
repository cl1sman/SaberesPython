# import turtle

# jorge = turtle.Turtle()
# print(jorge)
# jorge.shape('turtle')
# jorge.color('black', 'coral')
# jorge.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight) # my_screen is object, and canv is attribute
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l' # alinhando a esquerda (left)
print(table)