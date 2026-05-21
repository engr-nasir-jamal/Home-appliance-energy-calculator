import csv
from appliance import Appliance

# STEP 1: Load appliances from CSV

appliance_list = []

file = open("data.csv", "r")
reader = csv.reader(file)

for row in reader:
    name = row[0]
    power = float(row[1])

    device = Appliance(name, power, 0)
    appliance_list.append(device)

file.close()

# STEP 2: Show available appliances

print("\nAvailable Appliances:\n")

i = 0
for device in appliance_list:
    print(i, device.name, "-", device.power_watts, "W")
    i += 1

# STEP 3: User input (no duplicates allowed)

selected_devices = {}
used_indexes = set()

n = int(input("\nHow many appliances do you want to add? "))

for i in range(n):

    while True:
        print(str(i + 1) + ": Select appliance number")
        index = int(input())

        if index < 0 or index >= len(appliance_list):
            print("Invalid selection. Try again.")
            continue

        if index in used_indexes:
            print("Already selected. Choose another appliance.")
            continue

        used_indexes.add(index)
        break

    while True:
        quantity = int(input("Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        break

    while True:
        hours = float(input("Hours per day: "))

        if hours < 0 or hours > 24:
            print("Hours must be between 0 and 24.")
            continue

        break

    selected_devices[index] = (quantity, hours)

# STEP 4: Calculations

from calculator import daily_energy, daily_cost, monthly_energy, monthly_cost

results = []

for index, values in selected_devices.items():
    device = appliance_list[index]
    quantity = values[0]
    hours = values[1]

    daily = daily_energy(device.power_watts * quantity, hours)
    daily_cost_value = daily_cost(daily)
    monthly = monthly_energy(daily)
    cost = monthly_cost(monthly)

    results.append((device.name, daily, daily_cost_value, monthly, cost))

# STEP 5: Output report

print("\nEnergy Report")
print("----------------")

total_daily_energy = 0
total_daily_cost = 0
total_monthly_energy = 0
total_monthly_cost = 0

for result in results:
    print("Device Name:", result[0])
    print("Daily Energy Consumption:", round(result[1], 2), "kWh")
    print("Daily Cost:", round(result[2], 2), "Euro")
    print("Monthly Energy Consumption:", round(result[3], 2), "kWh")
    print("Monthly Cost:", round(result[4], 2), "Euro")
    print("----------------")

    total_daily_energy += result[1]
    total_daily_cost += result[2]
    total_monthly_energy += result[3]
    total_monthly_cost += result[4]

print("\nOverall Summary")
print("----------------")
print("Total Daily Energy Consumption:", round(total_daily_energy, 2), "kWh")
print("Total Daily Cost:", round(total_daily_cost, 2), "Euro")
print("Total Monthly Energy Consumption:", round(total_monthly_energy, 2), "kWh")
print("Total Monthly Cost:", round(total_monthly_cost, 2), "Euro")