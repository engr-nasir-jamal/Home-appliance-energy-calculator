def daily_energy(power_watts, hours_per_day):
    return (power_watts * hours_per_day) / 1000

def daily_cost(daily_energy):
    return daily_energy * 0.35

def monthly_energy(daily_kwh):
    return daily_kwh * 30

def monthly_cost(monthly_kwh, rate=0.35):
    return monthly_kwh * rate