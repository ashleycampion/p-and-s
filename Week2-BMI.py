# Programme for calculating BMI
# BMI formula is: weight-in-kgs / height-in-metres ** 2
# First store the user's input into variables, then plug them into the formula, and finaally print result to the screen

height = float(input("Enter height in centimetres:"))
weight = float(input("Enter weight in kgs:"))

bmi = weight / (height/100)**2

print("Your BMI is {:.2F}".format(bmi))
