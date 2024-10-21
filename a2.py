# Write a Python Program that asks for two numbers and Checks 
# If the number is Greater than the second 
# If the number is equal to the second 
# If the first Number is Less Than Equal to the Second

# We are taking User Input from the user as a First Number
a = int(input("Enter The First Number : "))
# We are taking User Input from the user as a Second Number
b = int(input("Enter The Second Number : "))
# Here We are Comparing a is greater than b or not by using > operator
if(a>b):  
    print(a," : Greater Than",b)
    # Here we are comparing a is equal to b or not using == operator 
elif(a==b): 
    print(a," : is Equal to", b)
    # Here we are comparing a is less than or equal to b using <= operator
elif(a<=b):  
    print(a, " : is Less Than Equal to", b)