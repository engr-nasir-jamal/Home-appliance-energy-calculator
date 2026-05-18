import csv
from appliance import Appliance

devices = []

file = open("data.csv", "r")
reader = csv.reader(file)

for row in reader:
    name = row[0]
    power = float(row[1])
    hours = float(row[2])

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

print("Energy Report")
print("----------------")

for result in results:
    print("Device Name:", result[0])
    print("Monthly Energy:", round(result[1], 2), "kWh")
    print("Monthly Cost:", round(result[2], 2), "Euro")
    print("----------------")