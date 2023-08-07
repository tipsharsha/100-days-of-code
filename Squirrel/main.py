import pandas
dict = {
    "Gray": 0,
    "Black": 0,
    "Cinnamon": 0,

}

squirrel_data = pandas.read_csv("Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data = squirrel_data["Primary Fur Color"].to_list()
for dat in data:

    if dat == "Black":
        dict["Black"] += 1
    if dat == "Gray":
        dict["Gray"] += 1
    if dat == "Cinnamon":
        dict["Cinnamon"] += 1

with open("Squirrel\squirrel_count.csv","w") as file:
    for dat in dict:
        file.write(dat + " " +str(dict[dat])+"\n")