"""
PLAIN ENGLISH

start create a list to store 5 numbers
capture 5 user inputs for the grades
each time we capture an input we append it to the list
sort the list in ascedning order then splice it starting at index 2
once we have the highest number we add them up and divide by 3
output a message to the user
end

PSEUDOCODE

create list 

capture input
append nunber to list

capture input
append nunber to list

capture input
append nunber to list

capture input
append nunber to list

capture input
append nunber to list

print message to user

"""

#code

grades = []
grade = input("Enter the 1st Grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd Grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd Grade: ")
grades.append(float(grade))

grade = input("Enter the 4th Grade: ")
grades.append(float(grade))

grade = input("Enter the 5th Grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades/3

print("average grade {0:.2f}%".format(result))