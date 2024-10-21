# Exercise 3: Logical Operators 
# Write a Python program that: 
# 1. Takes three boolean values (True or False) as input. 
#2. Uses and, or, and not operators to return the result of combining them. 
#Take input from the user
x1=bool(int(input("Enter the 1st no.:"))) 
#Take input from the user
x2=bool(int(input("Enter the 2nd no.: "))) 
#Take input from the user
x3=bool(int(input("Enter the 3rd no.: "))) 
#And Operator and result will be true only if all values are true
And=x1 and x2 and x3 
Or= x1 or x2 or x3
#Or Operator and result will be true if at least one of x1,x2 or x3 is true
Not= not x1
#Not Operator and result will be opposite of the x1
#Display the result
print("And Operator: ", And) 
#Display the result
print("Or Operator: ", Or) 
#Display the result
print("Not Operator: ", Not) 