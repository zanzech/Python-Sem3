temp = 42.0
if temp > 40:
    print("Cooling on")
print("Check done")

# temperature operating mode
temp = float(input("Enclosure temperature: "))
if temp < 20:
    mode = "heater on"
elif temp <= 45:
    mode = "normal"
elif temp <= 65:
    mode = "cooling"
else:
    mode = "emergency shutdown"
print("Operating mode:", mode)

# grade check
marks = 95
if marks >= 90:
    grade = "DISTINCTION"
elif marks >= 40:
    grade = "PASS"
else:
    grade = "FAIL"
print("Grade:", grade)
