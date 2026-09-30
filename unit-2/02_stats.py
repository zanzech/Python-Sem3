def stats(values):
    return sum(values) / len(values), min(values), max(values)

readings = [21.5, 23.2, 20.8, 24.5, 22.9]
mean, lo, hi = stats(readings)
print(f"mean = {mean:.2f} min = {lo} max = {hi}")

def greet(name):
    print("Hello", name)

res = greet("Titan")
print("returned:", res)

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))

def add_reading(data, value):
    data.append(value)

readings1 = [10, 20]
add_reading(readings1, 30)
print("modified:", readings1)

def rebind(data):
    data = [99]
    return data

readings2 = [10, 20]
rebind(readings2)
print("unchanged:", readings2)

def total_distance(points):
    total = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return total

d = total_distance([(0, 0), (3, 4)])
print("distance:", d)
