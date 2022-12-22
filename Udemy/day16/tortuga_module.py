# from turtle import Turtle, Screen

# tortuga = Turtle()
# tortuga.shape("turtle")
# tortuga.forward(200)
# tortuga.color("coral")


# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
print(table)
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = "l"
print(table)