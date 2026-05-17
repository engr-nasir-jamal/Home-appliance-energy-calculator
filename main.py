import csv
from appliance import Appliance

devices = []

file = open("data.csv", "r")
reader = csv.reader(file)

for row in reader:
    name = row["name"]
    power = float(row["power_watts"])
    hours = float(row["hours_per_day"])

    device = Appliance(name, power, hours)
    devices.append(device)

file.close()

from calculator import daily_energy, monthly_energy, monthly_cost
results = []

for device in devices:
    daily = daily_energy(device.power_watts, device.hours_per_day)
    monthly = monthly_energy(daily)
    cost = monthly_cost(monthly)

    results.append((device.name, monthly, cost))