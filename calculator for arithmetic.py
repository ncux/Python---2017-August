"""Calculator for basic arithmetic operations."""


# addition function
def add(x, y):
    return x + y


# subtraction function
def subtract(x, y):
    return x - y


# multiplication function
def multiply(x, y):
    return x * y


# division function
def divide(x, y):
    return x / y


print("Select an operation:")
print("A for addition")
print("S for subtraction")
print("M for multiplication")
print("D for division")

# Get user selection and input
selection = input("Enter a selection in CAPS:")
firstNum = int(input("Enter the first number:"))
secondNum = int(input("Enter the second number:"))

if selection == str('A'):
    print(firstNum, ' + ', secondNum, ' = ', add(firstNum, secondNum))
elif
    selection == str('S'):
    print(firstNum, ' - ', secondNum, ' = ', subtract(firstNum, secondNum))
elif
    selection == str('M'):
    print(firstNum, ' * ', secondNum, ' = ', multiply(firstNum, secondNum))
elif
    selection == str('D'):
    print(firstNum, ' / ', secondNum, ' = ', divide(firstNum, secondNum))
else:
    print('Invalid input. Try again.')












