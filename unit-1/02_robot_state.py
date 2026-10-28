name = "Titan"
battery = 85.5
docked = True
waypoints = 15

print(name)
print(type(name))
print(type(battery))
print(type(docked))
print(type(waypoints))

# battery update
battery = 100
print("start:", battery)
battery -= 15
print("after move:", battery)
battery -= 20
print("after scan:", battery)

# check battery level
battery = 42
if battery < 50:
    print("battery low, heading to dock")
print("status check done")

# 4 variables describing robot and warning if battery < 50
bot_name = "Orion"
bot_battery = 35.0
is_moving = True
tasks = 6

print(bot_name, bot_battery, is_moving, tasks)
if bot_battery < 50:
    print("Warning: Battery is low!")
