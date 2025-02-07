weight=float (input("Enter your weight in kg: "))
height=float (input( "Enter your height in metres: "))
BMI = weight/height**2
if BMI < 18.5:
    result = "underweight"
elif BMI <= 24.9:
    result = "normal"
elif BMI <= 29.9:
    result ="overweight"
elif BMI <= 34.9:
    result = " obese"
else:
    result = "extremely obese"
print({result})
print({BMI})


