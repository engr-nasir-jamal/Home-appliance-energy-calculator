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

    quantity = int(input("Quantity: "))

    while True:
        hours = float(input("Hours per day: "))

        if hours < 0 or hours > 24:
            print("Hours must be between 0 and 24.")
            continue

        break

    selected_devices[index] = (quantity, hours)

# STEP 4: Calculations

from calculator import daily_energy, monthly_energy, monthly_cost

results = []

for index, values in selected_devices.items():
    device = appliance_list[index]
    quantity = values[0]
    hours = values[1]

    daily = daily_energy(device.power_watts * quantity, hours)
    monthly = monthly_energy(daily)
    cost = monthly_cost(monthly)

    results.append((device.name, monthly, cost))

# STEP 5: Output report

print("\nEnergy Report")
print("----------------")

for result in results:
    print("Device Name:", result[0])
    print("Monthly Energy:", round(result[1], 2), "kWh")
    print("Monthly Cost:", round(result[2], 2), "Euro")
    print("----------------")