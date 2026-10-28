bot = "Titan"
battery = 76.452

print("Robot", bot, "at", battery, "%")
print(f"Robot {bot} at {battery}%")
print(f"Robot {bot} at {battery:.1f}%")
print(f"{bot:<10} | {battery:>5.2f}%")

# calculate runtime
cap = float(input("Enter battery capacity (mAh): "))
current = float(input("Enter current drawn (mA): "))
runtime = cap / current
print(f"Estimated runtime: {runtime:.2f} hours")
