THRESHOLD = 70.0

def is_alert(val):
    return val > THRESHOLD

def average(values):
    if not values:
        return 0
    return sum(values) / len(values)

if __name__ == "__main__":
    print("self test:", is_alert(85), average([10, 20, 30]))