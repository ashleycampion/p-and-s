# A programme tp reverse a string entered by the user, delete every second character, and print the resulting string to a screen.

# First store the user's input into a variable, then use the slice notation, variable[a:b:c],
# which means "count in increments of c starting at a inclusive, up to b exclusive".
# If c is negative you count backwards.
# If a is omitted then you start as far as possible in the direction you're counting from.
# If b is omitted then you end as far as possible in the direction you're counting to.
# See discussion here: https://stackoverflow.com/questions/21617586/reverse-string-string-1-works-but-string0-1-and-others-dont

x = input("Please enter a sentence: ")
print(x[::-2])
