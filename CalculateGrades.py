grades = []


# Calculate the total grade
def total_grade():
    total = 0

    for grade in range(0, len(grades)):
        total = total + grades[grade]
    return total


# Calculate the average of the grade
def calculate_average():
    return total_grade() / len(grades)


numberOfGrades = int(input("Enter number of grades: "))


for index in range(numberOfGrades):
    grades.append(float(input("Enter a valid grade: ")))


print('\nTotal Grade is ' + str(total_grade()))
print('Average: ' + str(calculate_average()))
print(grades)
