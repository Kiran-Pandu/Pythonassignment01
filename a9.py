# Write a Python program that:
# 1. Asks the user to input a list of 5 numbers.
# 2. Sorts the list in ascending order and displays it.
# 3. Sorts the list in descending order and displays it.

# we have Created the empty list
list=[]
# we are iterating through for loop upto 5 elements 
for i in range (5):
    #Taking User input from the user 
    a = input("Enter the List Elements : ")
    # Here We are adding elements in the list
    list.append(a)
    # we are printing Ordered List
print("The Normal List is : ",list)
# we are printing Ascedinnng  order List
print("The Ascending Order Of the List is : ",sorted(list))
# we are printing Descending  order List
print("The Descending Order Of the List is : ",sorted(list, reverse=True))