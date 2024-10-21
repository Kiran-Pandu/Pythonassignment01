# String Manipulation
# 1. Take a string input from the user.
# 2. Display the following:
# o The length of the string.
# o The first and last character.
# o The string in reverse order.
# o The string in uppercase and lowercase.

# Taking User Input from the user as a String Value
a = input("Enter A String Value : ") 
# Here We are Printing Orginal String
print(a) 
# Here We are Priting a Total Length of a String using len()
print(len(a)) 
# Here we are Printing Last element of the String
print(a[-1]) 
 # Here We are Reversing The String  
print(a[::-1])
# Here We are Converting String into Uppercase
print(a.upper()) 
# Here We are Converting String into Lowercase
print(a.lower()) 


