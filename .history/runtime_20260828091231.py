battery = 100
minutes =0
while battery >20:
    minutes +=1
    battery -=7
    print(f"Low battery alert after {minutes}minutes ({battery}%)")