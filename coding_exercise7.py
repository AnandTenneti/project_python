
#Initialisation of variables
weight = float(input("Enter weight in kg "))
height = float(input("Enter height in metres "))

#Caluclate bmi
bmi = round(weight/height**2,2)

# Checking different conditions for weight
if bmi<18.5:
    print(f"Your bmi is {bmi} and you are Underweight")
elif bmi<25:
    print(f"Your bmi is {bmi} and you are Normal weight")
elif bmi<28:
   print(f"Your bmi is {bmi} and you are overweight")
elif bmi<35:
    print(f"Your bmi is {bmi} and you are Obese")
else:
    print(f"Your bmi is {bmi} and you are clinically Obese")
