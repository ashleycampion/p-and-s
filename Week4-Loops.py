# Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# There is an ambiguity in the question, however:
# What if the user enters one?
# I chose not to end the program immediately in this case.
# In order not to end the program immediately if the user
# enters one, a 'while (x != 1)': loop will not work.
# Instead, a 'while true:' loop can be used, which breaks
# once 'x = 1'. I appreciate that 'while true:' is not
# generally considered best practice, but the absence of
# of a 'do-while' loop in python makes this unavoidable.

# Store the user's input as an integer.
x = int(input("Enter a positive integer and see what happens: "))
print(x)
# As there is no do-while loop built into Python,
# Use a 'while-true' loop that ends (with 'break') once the relevant variable equals one.
while True:
# To calculate the variable's next value, use an if-else block:
# to determine if the variable is even, use the modulus operator (x % 2 = 0);
# in all other cases the variable is odd.
    if x % 2 == 0:
        x = x // 2
        print(x)
    else:
        x = (x * 3) + 1
        print(x)
    if x == 1:
        break

I only used 'while True:' in order to replicate a do-while loop,
which I don't believe exists in Python (I thought it more intuitive not to end the program immediatley if the user entered one). I can change this to a 'while x != 1' of course, I'm just wondering is
there any way in Python to replicate what in Java would be 'do {...} while (x != 1)' without using 'while True:' and breaking when x = 1?
