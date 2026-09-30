battery = 100
minutes = 0
while battery > 20:
    battery -= 8
    minutes += 1
    print(f"minute {minutes} -> battery {battery}%")
print("battery low alert")

# input validation
while True:
    val = float(input("Enter battery % (0-100): "))
    if 0 <= val <= 100:
        break
    print("out of range, try again")
print("accepted:", val)

# countdown from 10 to 1
n = 10
while n >= 1:
    print(n)
    n -= 1
print("Lift off!")

# sum from 1 to 100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print("sum 1 to 100:", total)