#!/bin/usr/env python3

def Add(x,y):
    return x + y

def Substract(x,y):
    return x - y

def Multiply(x,y):
    return x * y

def Divide(x,y):
    return x / y

print('select operation')
print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')

choice = input('Enter choice 1/2/3/4:')
num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

if choice == '1':
    print(num1,'+',num2,'=',Add(num1,num2))
elif choice =='2':
    print(num1,'-',num2,'=',Substract(num1,num2))
elif choice == '3':
    print(num1, '*', num2, '=', Multiply(num1,num2))
elif choice == '4':
    print(num1,'/',num2,'=',Divide(num1, num2))
else:
    print('Invalid input')



