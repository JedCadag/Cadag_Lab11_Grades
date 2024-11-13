grades = []
sum_nums = 0  
for i in range(5):
    while True:
        try:
            grade = float(input(f"Enter grade for student {i+1} (40-100): "))
            if 40 <= grade <= 100:
                grades.append(grade)
                sum_nums += grade  
                break  
            else:
                print("Grade must be between 40 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("\nGrades inputted:", grades)
 
average_grade = sum_nums / len(grades)  
print("Average grade:", round(average_grade, 2))

passing_grades = [grade for grade in grades if grade >= 75]
num_passing = len(passing_grades)
print("Number of students with passing grade:", num_passing)

passing_percentage = (num_passing / len(grades)) * 100
print("Passing percentage:", round(passing_percentage, 2), "%")
