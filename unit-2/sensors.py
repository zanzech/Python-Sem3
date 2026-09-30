THRESHOLD = 70.0

def is_alert(val):
    return val > THRESHOLD

def average(values):
    if not values:
        return 0
    return sum(values) / len(values)

if __name__ == "__main__":
    print("sensors self test")
