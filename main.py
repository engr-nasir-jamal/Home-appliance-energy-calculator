import csv
from appliances import Appliance

devices = []

file = open("data.csv", "r")
reader = csv.reader(file)

for row in reader:
    name = row["name"]
    power = float(row["power_watts"])
    hours = float(row["hours_per_day"])

    appliances = Appliance(name, power, hours)
    devices.append(appliances)

file.close()