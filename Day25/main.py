# with open("weather_data.csv") as data:
#   weather_list = data.readlines()
# print(weather_list)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.remove(temperatures[0])
#     for i in range(len(temperatures)):
#         temperatures[i] = int(temperatures[i])
#
# print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data["temp"]))

# temp_list = data["temp"].to_list()
# print(len(temp_list))
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# print(data['temp'].max())
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp_monday_C = int(monday.temp)
# temp_monday_F = (temp_monday_C * 1.8) + 32
# print(temp_monday_F)

import pandas

data = pandas.read_csv("SQUIRRELS_CENTRAL_PARK.csv")
fur_color_list = data["Primary Fur Color"].to_list()

color_gray = 0
color_cinnamon = 0
color_black = 0
for fur in fur_color_list:
    if fur == "Gray":
        color_gray += 1
    elif fur == "Cinnamon":
        color_cinnamon += 1
    elif fur == "Black":
        color_black += 1

squirrels_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [color_gray,color_cinnamon,color_black]
}

data_squirrels = pandas.DataFrame(squirrels_dict)
data_squirrels.to_csv("new_data.csv")
