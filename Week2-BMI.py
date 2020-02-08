height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kgs:"))
bmi = weight / height**2
print("Your BMI is {:.2F}".format(bmi))

# Programme for calculating BMI
# BMI formula is: weight-in-kgs / height-in-metres ** 2

# First store the user's input into variables
height = float(input("Enter height in centimetres:"))
weight = float(input("Enter weight in kgs:"))
# then plug them into the formula
bmi = weight / (height/100)**2
# and finaly print result to the screen
print("Your BMI is {:.2F}".format(bmi))
