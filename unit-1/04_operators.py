heading = 355
turn = 15
print("raw:", heading + turn)
print("heading (0-359):", (heading + turn) % 360)
print("reverse:", (-45) % 360)

dist = 8.5
limit = 10
print(dist < limit)
print(dist == limit)
print(0 <= dist < limit)

battery = 45
print(dist > 5 and battery > 20)
print(dist > 5 or battery > 90)

# robot safe to move check: distance > 10, battery > 20, not docked
d = 30
b = 60
docked = False
safe = d > 10 and b > 20 and not docked
print("safe to move:", safe)