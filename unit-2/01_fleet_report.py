def battery_band(pct, name="Titan"):
    if pct < 15:
        print(f"{name}: CRITICAL")
    elif pct < 30:
        print(f"{name}: LOW")
    else:
        print(f"{name}: OK")

battery_band(10, "Alpha")
battery_band(25, "Beta")
battery_band(80)

def classify(pct):
    if pct < 15:
        return "critical"
    elif pct < 30:
        return "low"
    return "OK"

fleet = {"Alpha": 10, "Beta": 25, "Gamma": 80, "Delta": 45}
for name, pct in fleet.items():
    print(f"{name:<7} {pct:>3}% {classify(pct)}")

def area(r):
    return 3.14 * r * r

total = area(2) + area(3)
print("area total:", total)

def move_robot(x, y, speed=1.0):
    print(f"moving to ({x}, {y}) at speed {speed}")

move_robot(2, 5)
move_robot(2, 5, 0.5)
move_robot(y=5, x=2)

def log(*values, **options):
    print("values:", values)
    print("options:", options)

log("start", 1, 2)
log("alert", level="high")

# default argument pattern
def add_waypoint(wp, route=None):
    if route is None:
        route = []
    route.append(wp)
    return route

r1 = add_waypoint((0, 0))
r2 = add_waypoint((4, 4))
print("r1:", r1)
print("r2:", r2)
print("same object?", r1 is r2)