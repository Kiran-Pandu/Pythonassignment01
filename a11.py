# Empty list to store students data
Students = []     
# Take input for 3 stdents
for i in range(3):    
    name = input (f"Enter the name of student{i+1}: ")
    # To take the 3 scores for each student
    Scores = []
    for j in range(1,4):
        score = int (input(f"Enter the score of subject{j} for {name}: "))
        scores.append(score)
    # To store name and scores of students in nested list
    students.append([name, scores])
# Calculate and display the name and average score
for student in students:
    name = student[0]
    scores = student[1]
# calculate the average score
    ave_sco = sum(scores)/len(scores)    
    print (f"{name}'s average score is: {ave_sco:.2f}") 
