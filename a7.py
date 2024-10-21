
# Write a Python program that:
# 1. Creates a list of 5 numbers (input from the user).
# 2. Displays the sum of all the numbers in the list.
# 3. Finds the largest and smallest number in the list.

#creating an empty list
list = []
# we iterating each list element through for loop to store in List
for i in range (5):
    #We are taking 5 user input from the user as a Numbers
    b=int(input("Enter 5 Numbers : "))
    # Here we are Inserting  elements to the list through append() Built-in Function
    list.append(b) 
    # We finding The sum of all list elements Using sum() Built-in Function
c = sum(list) 
# We finding The Maximum Number in the List Using Max() Built-in Function
d = max(list)
# We finding The Minimum Number in the List Using min() Built-in Function 
e = min(list) 
# Here We are printing The List
print("The List is : ",list) 
# We are printing Sum of list
print("The sum of List is : ",c) 
#we are printing max number in the list
print("The Maximum Number in List is : ",d) 
#we are printing min number in the list
print("The Minimum Number in List is : ",e) 



