count = 0
def tick():
    count = 0
    count += 1
    return count

print(tick(), tick(), count)

THRESHOLD = 70
def is_alert(val):
    return val > THRESHOLD

print(is_alert(85), is_alert(50))

# global variable update
ticks = 0
def increment():
    global ticks
    ticks += 1
    return ticks

print(increment(), increment(), increment())
print("global ticks:", ticks)

def step(c):
    return c + 1

val = 0
val = step(val)
val = step(val)
print("count:", val)

def make_report():
    lines = ["header", "body"]
    return len(lines)

print(make_report())
print("lines in global:", "lines" in dir())