# TODO get hold of weather_data.csv file using with open method
# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
#     print(weather_data)

# TODO import and use CSV module. CSV module is python pre-build library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in list(data)[1:]:
#         temperature.append(int(row[1]))
#     print(temperature)

# TODO using of pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
# 'Type' will tell the type of file. For ex. full spreadsheet is a 'Data Frame' while 1 column/row is 'Series '

# print(type(data))
# print(type(data["temp"]))

# TODO print the whole spreed sheet
# print(data)

# TODO print particular column(s) by there heading
# print(data["temp"])

# TODO convert the sheet to a dict
# data_dict = data.to_dict()
# print(data_dict)

# TODO convert column(s) into a list calling by it's heading
temp_list = data["temp"].to_list()
# print(temp_list)

# condition_list = data["condition"].to_list()
# print(condition_list)

# TODO getting average temp from all the data (old way - 1, by for loop)
# length = len(temp_list)
# total = 0
# for i in temp_list:
#     total += i
# avg = round(total / length, 2)
# print(f"Average Temperature is {avg}")

# TODO getting average temp from all the data (old way - 2, by for loop)
# avg = round(sum(temp_list) / len(temp_list), 1)
# print(avg)

# TODO getting average temp from all the data using pandas pre-builds functions
# print(data['temp'].mean())
# print(data['temp'].max())

# print(condition_list.count('Sunny'))

# TODO Get data in columns
# print(data['condition'])
# print(data.condition)

# TODO Get data in Row
# print(data[data.day == 'Monday'])

# TODO get row with highest temp
# print(data[data.temp == data.temp.max()])

# OR

# max_temp = (data['temp'].idxmax())
# print(data.iloc[max_temp])
# print(data.loc[max_temp])

# TODO get hold of item(s) in a row
# monday = data[data.day == 'Monday']
# print(monday.day)
# print(monday.temp)
# print(monday.condition)

# TODO Convert Celsius to Fahrenheit --v1
# monday = data[data.day == 'Monday']
# c = int(monday.temp)
# f = (c * 9 / 5) + 32
# print(f"Temp is {f}°F and {c}°C")

# TODO Convert Celsius to Fahrenheit --v2
# monday = data[data.day == 'Monday']
# f = (int(monday.temp) * 9 / 5 + 32)
# print(f"Temp is {f}°F and {int(monday.temp)}°C")

# TODO Convert Celsius to Fahrenheit --version Udemy
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# TODO Create a DataFrame from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# print(data2)

# TODO Save the DataFrame to .csv
# data2.to_csv("new_data.csv")


