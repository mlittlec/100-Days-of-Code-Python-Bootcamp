# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()
print(len(temp_list))


average = sum(temp_list) / len(temp_list)
print(average)


print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])


# Get the row of data which has the highest temperature in the week
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Extract the data for the temperature and convert it into Farenheit
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32

print(monday_temp_F)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_data = pandas.DataFrame(data_dict)
data.to_csv("my-new-data.csv")
print(my_data)
