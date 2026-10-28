raw = "   Titan Rover   "
print(f"[{raw}]")
print(f"[{raw.strip()}]")
print(raw.strip().lower())
print(raw.strip().upper())
print(raw.strip().replace(" ", "_"))
print("Rover" in raw)

packet = "T:28;H:65;B:82"
fields = packet.split(";")
print("fields:", fields)
for field in fields:
    key, val = field.split(":")
    print(key, "->", float(val))

# custom packet format
telemetry = "lat:12.97;lon:77.59;amps:2.4"
parts = telemetry.split(";")
for item in parts:
    sensor, reading = item.split(":")
    print(sensor, "=", float(reading))