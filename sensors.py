threshold = 70.0

def is_alert(value):
    return value > threshold

def average(values):
    return sum(values) / len(values)

if __name__ == "__main__":
    print("Self-test:", is_alert(85), average([10, 20, 30, 40]))

