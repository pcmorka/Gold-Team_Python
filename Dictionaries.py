"""
#Interactive Coding Exercise] Grading Program
"""

student_scores = {
  "Harry": 82,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 75,
  "Neville": 64,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
     student_grades[student] = "Outstanding"
    elif score > 80:
     student_grades[student] = "Exceeds Expectations"
    elif score > 70:
     student_grades[student] = "Acceptable"
    else:
     student_grades[student] = "Fail"

    

# 🚨 Don't change the code below 👇
print(student_grades)

