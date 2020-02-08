<<<<<<< HEAD
height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kgs:"))
bmi = weight / height**2
print("Your BMI is {:.2F}".format(bmi))

=======
# Programme for calculating BMI
# BMI formula is: weight-in-kgs / height-in-metres ** 2
# First store the user's input into variables, then plug them into the formula, and finaally print result to the screen

height = float(input("Enter height in centimetres:"))
weight = float(input("Enter weight in kgs:"))

bmi = weight / (height/100)**2

print("Your BMI is {:.2F}".format(bmi))
>>>>>>> b34a1006f9b89b0e2a30939271a3e024d84e208b
