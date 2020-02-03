# Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Store the user's input as an integer.
# As there is no do-while loop built into Python,
# Use a 'while-true' loop that ends (with 'break') once the relevant variable equals one.
# To calculate the variable's next value, use an if-else block:
# to determine if the variable is even, use the modulus operator (x % 2 = 0);
# in all other cases the variable is odd.


x = int(input("Enter a positive integer and see what happens: "))

print(x)

while True:
    if x % 2 == 0:
        x = x // 2
        print(x)
    else:
        x = (x * 3) + 1
        print(x)
    if x == 1:
        break
