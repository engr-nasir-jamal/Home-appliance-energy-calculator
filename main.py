import csv
from appliance import Appliance

# STEP 1: Upload appliances from CSV file

appliance_list = []

file = open("data.csv", "r")
reader = csv.reader(file)

# Read each row from CSV and create Appliance objects
for row in reader:
    name = row[0]                                       # appliance name
    power = float(row[1])                               # power in watts

# Create object with 0 hours (hours will come from user input later)
    device = Appliance(name, power, 0)
    appliance_list.append(device)

file.close()

# STEP 2: Display available appliances

print("\nAvailable Appliances:\n")
i = 0
for device in appliance_list:
    print(i, device.name, "-", device.power_watts, "W")
    i = i + 1

# STEP 3: User selects appliances

selected_devices = []

# How many different appliances user wants to calculate for
n = int(input("\nHow many appliances do you use? "))

for i in range(n):
    index = int(input("Select appliance number: "))

# Validate index to avoid invalid selection
    if index < 0 or index >= len(appliance_list):
        print("Invalid selection. Try again.")
        continue

    quantity = int(input("Quantity: "))                 # number of same devices
    hours = float(input("Hours per day: "))             # usage per day

    device = appliance_list[index]

# Store selected appliance with user inputs
    selected_devices.append((device, quantity, hours))

# STEP 4: Energy + cost calculations

from calculator import daily_energy, monthly_energy, monthly_cost

results = []

for item in selected_devices:
    device = item[0]
    quantity = item[1]
    hours = item[2]

# Calculate energy usage
    daily = daily_energy(device.power_watts * quantity, hours)
    monthly = monthly_energy(daily)
    cost = monthly_cost(monthly)

# Store final result
    results.append((device.name, monthly, cost))

# STEP 5: Display final report

print("\nEnergy Report")
print("----------------")

for result in results:
    print("Device Name:", result[0])
    print("Monthly Energy:", round(result[1], 2), "kWh")
    print("Monthly Cost:", round(result[2], 2), "Euro")
    print("----------------")