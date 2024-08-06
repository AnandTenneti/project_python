#caluclate the BMI 
weight = float(input("Enter the weight (in kgs) : "))
height = float(input("Enter the height (in metres) : "))

bmi = weight/(height**2)

print("The BMi of a person is ", bmi)