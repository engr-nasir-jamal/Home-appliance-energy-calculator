def daily_energy(power_watts, hours_per_day):
    return (power_watts * hours_per_day) / 1000

def monthly_energy(daily_kwh):
    return daily_kwh * 30

def monthly_cost(monthly_kwh, rate=0.30):
    return monthly_kwh * rate