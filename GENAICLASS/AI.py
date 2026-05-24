#a = "Hi,pavan"   
#print(a[0:5])

#forloop

#a = "Hi,Pavan"
#for x in a:
    #print(x)

#a = "Hi,Pavan"
 #print(len(a))
#for x in range(0, len(a)):
    #print(a[x])  # 


#x = 0
#while x <= 9:
 #      print(x)
#       x += 1


#n1 = input("Give your name")
#n1 ="Adithya"
#print(n1)
#print(type(n1))


number = input("Give the number to check even or odd")

pho = int(number)
print(pho)
print(type(pho))
print(pho/5)
print(number/5)


reminder and divided by 2 even number or odd number ,if odd number print , if even number dont print

define 

def print_name(name):
    return(f"hello {name}")

a = print_name("pavan")
print(a)


def calculator(num1, num2, operd):
    if operd == '+':
        return num1 + num2
    elif operd == '-':
        return num1 - num2
    elif operd == '*':
        return num1 * num2
    elif operd == '/':
        return num1 / num2

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
operd = input("Enter your operand (+,-,/,*)")
result = calculator(num1, num2, operd)
print(result)


----------------------------------------------------------------------------------
def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):  #a = 20, b = 5
    if a > b:  # 20 > 5
        return(a/b)  # 20/5
    else:
        return(b/a)

def calculator(num1, num2, operd):
    if operd == '+':
        print(add(num1,num2))
    elif operd == '-':
        print(sub(num1,num2))
    elif operd == '*':
        print(mul(num1,num2))
    elif operd == '/':
        print(div(num1,num2))

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
operd = input("Enter your operand (+,-,/,*)")
result = calculator(num1, num2, operd)
print(result)
============================================================================================
if the user want to get two to the power 2 , in python how could we know it is python  , put it in git link and give 



num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
operd = input("Enter your operand (+,-,/,*)")
result = calculator(num1, num2, operd)

def calculator(num1, num2, operd):
    if operd == '+':
        print(add(num1,num2))
    elif operd == '-':
        print(sub(num1,num2))
    elif operd == '*':
        print(mul(num1,num2))
    elif operd == '/':
        print(div(num1,num2))

print(result)
==============================================================================================================

operd = input("Enter your operand (+,-,/,*, pow)")
if operd == "pow":
    base = int(input("Enter a base"))
    power = int(input("Enter a power"))
else:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
result = calculator(num1, num2, operd)

def calculator(num1, num2, operd):
    if operd == '+':
        print(add(num1,num2))
    elif operd == '-':
        print(sub(num1,num2))
    elif operd == '*':
        print(mul(num1,num2))
    elif operd == '/':
        print(div(num1,num2))

print(result)

==============================================================================================================================


def calculator(num1, num2, operd):
    if operd == '+':
        add = lambda num1, num2 : num1 + num2
    elif operd == '-':
        print(sub(num1, num2))
    elif operd == '*':
        print(mul(num1, num2))
    elif operd == '/':
        print(div(num1, num2))

=============================================================================================================================
read about daet time 
popular modules 
import math
import json 

from calculator import *

def calculator(num1, num2, operd):
    if operd == '+':
        print(add(num1, num2))
    elif operd == '-':
        print(sub(num1,num2))
    elif operd == '*':
        print(mul(num1,num2))
    elif operd == '/':
        print(div(num1,num2))

operd = input("Enter your operand (+,-,/,*, pow)")
if operd == "pow":

    def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):  #a = 20, b = 5
    if a > b:  # 20 > 5
        return(a/b) # 20/5
    else:
        return(b/a)
