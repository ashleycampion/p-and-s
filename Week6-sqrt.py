# Write a program that takes a positive floating-point
# number as input and outputs an approximation of its square
# root. You should create a function called sqrt that does this.

# I will provide two solutions to demonstrate how significant
# the difference in efficiency between algorithms can be.
# The first is a brute force solution, wonderfully inefficient
# for large input values.
# The second will use Newton's algorithm, whose efficiency
# depends on the accuracy desired rather than the number input.
# I didn't both timing them, as that's beyond the scope of this.

# Solution 1
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



print("Please enter a positive number and I'll brute force its square root")
x = float(input("( make it less than 999999, unles you're veeeeerrrrry patient): "))

print("The square root of " + str(x) + " is approximately " + str(square(x)))


# Solution 2
# Newton's algorithm:
# better guess = 0.5 * (guess + number/ guess)
def newton(x):
    # have the function take a guess
    guess = x / 2
    # while the guess is not of a sufficient accuracy,
    # apply Newton's algorithm to improve it.
    # To check the accuracy of the guess, square it and
    # check the difference between the result and the input.
    while abs(guess ** 2 - x) > x / 1000000:
        # apply Newton's alogrithm
        guess = 0.5 * (guess + x / guess)
        # once the guess is sufficiently accurate the while
        # loop ends. Now round the result to your liking
    return round(guess, 1)

x = float(input("Please enter another positive number (as large as you'd like): "))

print("The square root of " + str(x) + " according to Newton (and the Babylonians) is approximately " + str(newton(x)))

