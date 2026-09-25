# Write a function called add_all_nums which takes arbitrary number of arguments
# and sums all the arguments. Check if all the list
# items are number types. If not do give a reasonable feedback.
# def add_all_nums(*nums):
#     final=0
#     for n in nums:
#         if not isinstance(n,(int,float)):
#             return f"This {n} is not a number.Please give a Number."
#         final+=n
#     return final

# print(add_all_nums(4,5,6)) 
# print(add_all_nums(4,5,'ahhhh'))   
    


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# def convert_celsius_to_fahrenheit(C):
#     f=(C*9/5)+32
    
#     return f

# print(convert_celsius_to_fahrenheit(5))
# Write a function called calculate_slope which return the slope of a linear equation

# def calculate_slope(x1,y1,x2,y2):
#     m=(y2-y1)/(x2-x1)

#     return m

# print(calculate_slope(4,5,6,8))
    
# def countdown(n):
#     if n==0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(2)
def factorial(n):
    if n == 1:
        return 1                     # FIXED — return the value, not just print a message
    else:
        result = n * factorial(n - 1)
        
        return result                 # also should return, so outer calls can use it!

print(factorial(3))
