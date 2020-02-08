# Program to calculate grade based on percentage
# Too trivial to annotate

percent = float(input("Enter your grade: "))
if percent < 40:
    print("Fail")
elif percent < 49.5:
    print("Pass")
elif percent < 59.5:
    print("Merit 2")
elif percent < 69.5:
    print("Merit 1")
else:
    print("Distinction")


# Program to read in numbers and calculate average

answers = []
answer = int(input("Enter a number (0 to quit): "))

# To ensure 0 will not be added to the array
# Which would mess up the average,
# Check if zero before appending to array
while answer != 0:
    answers.append(answer)
    answer = int(input("Enter a number (0 to quit): "))

for x in answers:
    print(f"You entered: {x}")

# To ensure against division by zero
if len(answers) > 0:
    print(f"Average is {sum(answers)/len(answers)}")



# A program that reads in students' names
# And prints them back once the user
# enters nothing for a first name

# Simply store input in two arrays and print afterwards
# By iterating through both at the same time
firstNames = []
lastNames = []

fName = input("Enter first name of student (enter blank to quit): ")

while len(fName) > 0:
    lName = input("Enter last name of student: ")
    firstNames.append(fName)
    lastNames.append(lName)
    fName = input("Enter first name of next student (enter blank to quit): ")

for x, y in zip(firstNames, lastNames):
    print(f"{x} {y}")


# Program that generates 10 random numbers (0-100)
# prints them out then prints out the top three

import random as r
# Store numbers in an array, sort it in descending order
# then print out first three
numbers=[]
for i in range(10):
    x = r.randint(0, 100)
    print(x)
    numbers.append(x)
numbers.sort(reverse=True)
print(f"Highest numbers are: {numbers[:3]}")




