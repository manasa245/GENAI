#if the user want to get two to the power 2 , in python how could we know it is python  , put it in git link and give #

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def calculator(num1, num2, operd):
    if operd == '+':
        return add(num1, num2)
    elif operd == '-':
        return sub(num1, num2)
    elif operd == '*':
        return mul(num1, num2)
    elif operd == '/':
        return div(num1, num2)
    elif operd == '**':
        return power(num1, num2)
    else:
        return "Invalid operand"

# User inputs
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operd = input("Enter your operand (+,-,/,*,**): ")

# Calculate and print result
result = calculator(num1, num2, operd)
print(result)