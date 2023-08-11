# TODO import pandas
import pandas

# TODO read csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data['Primary Fur Color'])

# TODO get hold of and convert the Primary Fur Color COLUMN to list
fur_color_list = data['Primary Fur Color'].to_list()

# TODO add all the colors to a list with for loop
colors = []

for color in fur_color_list:
    if color not in colors:
        colors.append(color)

print(colors)

# TODO get the total numbers of squirrel by color
total_gray = fur_color_list.count('Gray')
total_cinnamon = fur_color_list.count('Cinnamon')
total_black = fur_color_list.count('Black')

# print(f"Total Gray are {total_gray}, Black are {total_black} & Cinnamon are {total_cinnamon}")

# TODO convert the data into dictionary
data_dict = {
    "Fur Color": colors[1:],
    "Count": [total_gray, total_cinnamon, total_black]
}

# TODO convert the dict to CSV
color_data = pandas.DataFrame(data_dict)
color_data.to_csv('color_data.csv')
print(color_data)

