# battery = 100
# minutes =0
# while battery >20:
#     minutes +=1
   
#     print(f"Low battery alert after {minutes}minutes ({battery}%)")

# print("alert ")

# while True:
#     text = input("enter battery %(0-100): ")
#     value = float(text)
    
       

    
#     if 0<= value <= 100:
#         break
#     print("Invalid input. Please enter a number between 0 and 100.")
# print("accaepted",value)

list=[]
n= int(input("enter the number of elements in the list: "))
for i in range(n):
    number=int(input("enter the number: "))
    list.append(number)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            tmp=list[i]
            list[i]=list[j]
            list[j]=tmp
print("The sorted list is: ",list)
