import sensors
from sensors import is_alert
import sensors as sn

readings = [60, 85, 72]
print("threshold:", sensors.THRESHOLD)
print("average:", sensors.average(readings))

for r in readings:
    print(r, "->", "ALERT" if sensors.is_alert(r) else "ok")

print("via sensors:", sensors.is_alert(85))
print("via is_alert:", is_alert(85))
print("via sn:", sn.is_alert(85))

print("__name__ in main.py:", __name__)
print("__name__ in sensors.py:", sensors.__name__)