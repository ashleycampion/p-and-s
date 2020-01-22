height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kgs:"))
bmi = weight / height**2
print("Your BMI is {:.2F}".format(bmi))
