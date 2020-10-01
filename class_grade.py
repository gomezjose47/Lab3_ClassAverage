



"""
start
create a list to store 5 numbers(float)
capture user's input 5 times for their grades
each time we capture thee user's input, we append the number to the list
sort the list ascending, then splice the items at index 2
once we have three highest number in the list, we sum them up and dividie by 3
output a message to the user
end
"""


""" 
create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

Print message to user
"""


grades = []

grade = input("enter the 1st grade: ")
grades.append(float(grade))

grade = input("enter the 2nd grade: ")
grades.append(float(grade))

grade = input("enter the 3rd grade: ")
grades.append(float(grade))

grade = input("enter the 4th grade: ")
grades.append(float(grade))

grade = input("enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades=[2:]

grades = sum(grades)

result = grades / 3

print("Average grade {0:.2f}%".format(result))
