# Write a program that takes a positive floating-point
# number as input and outputs an approximation of its square
# root. You should create a function called sqrt that does this.
# I will try this without using the sqrt function in Math module,
# This will thus not be an efficient solution, but it is
# interesting to try.

# First create a function 'square', then apply it to the
# number entered by the user.

# We will be using the Math.ceil function
import math

def square(x):
    # create a variable to store the answer in
    closest = 0
    # as this is only an approximate calculation, i.e.
    # to only one decimal place, we can iterate through
    # the numbers between 0 and the input in steps of 0.1
    # and then find which number when squared is closest
    # to the input. Because Python's for loop does not allow
    # stepping in non-integer values, we have to get creative.
    # One option is to iterate through the numbers up to the input,
    # and then for each number (i) use a list comprehension to cycle
    # from i to i+1 in steps of 0.1. For accurate answers for an
    # input of less than 1, we will need to Math.ceil the input,
    # as the answer might be larger than the input (but less than 1).
    for i in range(0, math.ceil(x)):
        for k in [i + j / 10 for j in range(10)]:
            # if the current answer is more accurate than the best answer up to
            # the current iteration, store it in 'closest,' else ignore it
            closest = k if (abs(x - k ** 2) < abs(x - closest ** 2)) else closest
    return closest




x = float(input("Please enter a positive number: "))

print("The square root of " + str(x) + " is approximately " + str(square(x)))
