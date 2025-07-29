# Assignment-1(Task 1)
def math_operations(num1, num2):
    print("Addition: ", num1 + num2)
    print("Subtraction: ", num1 - num2)
    print("Multiplication: ", num1 * num2)

    if num2 != 0:
        print("Division: ", num1 / num2)
    else:
        print("Division: Error! Cannot divide by zero.")

# Take user input
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Call the function
    math_operations(num1, num2)

except ValueError:
    print("Invalid input! Please enter numeric values.")
