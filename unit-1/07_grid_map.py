waypoints = [(0, 0), (1, 3), (4, 5)]
for wp in waypoints:
    print("moving to", wp)

for i in range(1, 6):
    print(i, end=" ")
print()

for i in range(10, 0, -2):
    print(i, end=" ")
print()

readings = [21.5, 23.0, 22.8, 24.2, 23.5]
total = 0
for r in readings:
    total += r
print(f"sum: {total:.2f}")
print("count:", len(readings))
print(f"mean: {total/len(readings):.2f}")

# 8x8 grid with obstacles, S at (0,0) and G at (7,7)
obstacles = [(2, 3), (4, 1), (5, 6)]
for i in range(8):
    for j in range(8):
        if (i, j) == (0, 0):
            print("S", end=" ")
        elif (i, j) == (7, 7):
            print("G", end=" ")
        elif (i, j) in obstacles:
            print("X", end=" ")
        else:
            print(".", end=" ")
    print()

readings = [15, -1, 32, 85, 20]
for r in readings:
    if r < 0:
        continue
    if r > 70:
        print("Danger reading:", r)
        break
    print("safe reading:", r)
