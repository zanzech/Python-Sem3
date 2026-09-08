# battery = 100
# minutes =0
# while battery >20:
#     minutes +=1
   
#     print(f"Low battery alert after {minutes}minutes ({battery}%)")

# print("alert ")

while True:
    text = input("enter battery %(0-100): ")
    value = float(text)
        
       

    
    if 0<= value <= 100:
        break
    print("Invalid input. Please enter a number between 0 and 100.")
print("accaepted",value)