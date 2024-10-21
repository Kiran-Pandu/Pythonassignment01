# Write a Python program that:
# 1. Asks for a sentence input from the user.
# 2. Asks for a word to search in the sentence.
# 3. Outputs whether the word exists in the sentence and, if it does, 
# at which position (index).

# Taking User Input from the user as Sentence
sentence = input("Enter Sentence : ") 
# Taking User Input from the user as Word
word = input("Enter a word : ") 
# We are Checking whether word in present in sentence or not through if block
if word in sentence:  
    # Here We are taking the index of a word
    index = sentence.index(word) 
    # if the word is present in the sentence then it will print if block
    print(word, "Exists in the sentence and its index is : ", index)  
# if the word is not present in the sentence then it will print else block
else:
    print(word,"does not exist in this sentence : ", sentence)