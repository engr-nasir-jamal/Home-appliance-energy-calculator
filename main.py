import csv
from appliance import Appliance

# Appliances from CSV
appliance_list = []

file = open("data.csv", "r")
reader = csv.reader(file)

for row in reader:
    name = row[0]
    power = float(row[1])

    device = Appliance(name, power, 0)
    appliance_list.append(device)

file.close()

# Show list
print("\nAvailable Appliances:\n")

i = 0
for device in appliance_list:
    print(i, device.name, "-", device.power_watts, "W")
    i = i + 1

# User input system
selected_devices = []

n = int(input("\nHow many appliances do you use? "))

for i in range(n):
    index = int(input("Select appliance number: "))

    if index < 0 or index >= len(appliance_list):
        print("Invalid selection. Try again.")
        continue

    quantity = int(input("Quantity: "))
    hours = float(input("Hours per day: "))

    device = appliance_list[index]

    selected_devices.append((device, quantity, hours))

# Calculations
from calculator import daily_energy, monthly_energy, monthly_cost

results = []

for item in selected_devices:
    device = item[0]
    quantity = item[1]
    hours = item[2]

    daily = daily_energy(device.power_watts * quantity, hours)
    monthly = monthly_energy(daily)
    cost = monthly_cost(monthly)

    results.append((device.name, monthly, cost))

print("\nEnergy Report")
print("----------------")

for result in results:
    print("Device Name:", result[0])
    print("Monthly Energy:", round(result[1], 2), "kWh")
    print("Monthly Cost:", round(result[2], 2), "Euro")
    print("----------------")
