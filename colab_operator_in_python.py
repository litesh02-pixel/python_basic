# -*- coding: utf-8 -*-
"""Operator_in_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10RH2ioGlcv101yPKnW_TRb9Kn-LODFgV

#Arithmatic Operator in Pythons
"""

n1 = 20
n2 = 10
#Addition
sum = n1 + n2
print("Sum= ",sum)

#Subtraction
sub = n1 - n2
print("Difference= ", sub)

#Multiplication
mul = n1*n2
print("Multiplication= ", mul)

#Division
div = n1/n2
print("Division= ", div)

#Division
div = n1//n2
print("Division= ", div)

#Exponential
exp = n1**n2
print("Exponential= ", exp)

#moulus
mod = n1%n2
print("Modulud= ", mod)

"""# Assignment Operator
### assigning a value to variable


"""

a = 5
print(a)
# += operator
a +=5
print(a)

# -= operator
b = 10
print(b)
b -= 2
print(b)

# *= operator

a *= 5
print(a)

"""#Comparision Operator

"""

a = 5
b = 10
print(a == b)
print(a!=b)
print(a>b)
print(a<b) 
print(a<=b)
print(a>=b)

"""#Logical Operator"""

a = 10 
print(a>20 and a<5)
print(a>5 and a<20)
print(a>20 or a<5)
print(not(a>8 and a>5))

"""#Identity Operator"""

x = 5
y = 5
print(x is y)
print(x is not y)

x = 5
y = 10
print(x is y)
print(x is not y)

"""#Membership Operator"""

a = 5
b = 10
c = [1,2,3,4,5,6]

print(a in c)
print(b in c)

a = 5
b = 10
c = [1,2,3,4,5,6]

print(a not in c)
print(b not in c)

