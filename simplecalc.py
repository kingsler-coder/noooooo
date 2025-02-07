# prompt the user for two numbers
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# prompt the user to enter operator
operator=input("Enter an operator (+,_,*,/)")
# perform calculation based on operation
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num2 - num1)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        result =num1 / num2
        print(num1/num2)
    else:
        print("Error , divisible by zero")
else:
    result="Invalid Operator"
    print(f"The answer is {result}")

