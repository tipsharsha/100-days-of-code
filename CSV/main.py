"""using csv files"""

from calendar import day_abbr
import csv
from dataclasses import dataclass
import pandas


# with open("doturn35to2601-do1704__Forced_Replay_File_with_filters.csv") as file:
#     file_data = csv.reader(file)
#     for row in file_data:
#         print(row)
#     print(type(file_data))


data = pandas.read_csv("weather_data.csv")
print(data.condition)

print(data[data.temp == data["temp"].max()])
print(data[data.day == "Monday"].temp)
    