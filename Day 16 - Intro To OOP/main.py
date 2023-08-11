# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('green')
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

table.add_column("Person's name", ['Person1', 'Person2', 'Person3', 'Person4', 'Person5'])
table.add_column("Person's Age", [20, 19, 22, 20, 21])
table.add_column("Occupation", ['Student', 'Student', 'Student', 'Student', 'Student'])
table.add_column("Department", ['IT', 'IT', 'IT', 'IT', 'IT'])

table.border = False
table.align = 'l'
table.header_style = 'upper'

print(table)
