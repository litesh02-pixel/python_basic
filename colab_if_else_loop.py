# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QeIm5xTQCm_iqTo0KohhQW1uAp4mAaDO

#if else loop
"""

a = 30
b = 50
if (a>b):
  print("a is greater number")
else:
  print("b is greater number")

x = 9
r = x % 2
if r == 0:
  print("Even Number")
else:
  print("Odd Number")

"""#if elif else"""

x = 2
if (x==1):
  print("One")
elif (x==2):
  print("Two")
elif (x==3):
  print("Three")
else:
  print("Wrong Input")

#if elif else
x = 4
if (x==1):
  print("One")
elif (x==2):
  print("Two")
elif (x==3):
  print("Three")
else:
  print("Wrong Input")

# if elif else
a = 10
b = 20
c = 30
if (b<a>c):
  print("a is greater number")
elif (a<b>c):
  print("b is greater number")
else:
  print("c is greater number")

"""# nested if """

x = 7
r = x%2
if (r==0):
  print("Even Number")
  if (x>5):
    print("Greater Number")
  else:
    print("Not Greater")
else:
  print("Odd Number")

a = 20
b = 30
c = 10
if (a>b):
  if (a>c):
    print("a is the greatest number")
  else:
    print("c is the greatest number")
else:
  if (b>c):
    print("b is the greatest number")
  else:
    print("c is the greatest number")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if (a>b):
  print("a is greater")
else:
  print("b is greater")

