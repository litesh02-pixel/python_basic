# -*- coding: utf-8 -*-
"""loops_for_while.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujLJNkBFFxV76zj6QINJlE5nC-aYmvkX
"""

#for loop

for i in range(5):
  laptop_price=int(input("Enter the price of laptop: "))

#for loop for list

nums=[10,20,30,40,50]
for i in nums:
  print(i)

for i in range(10):
  print(i)

for i in range(11,21,1):
  print(i)

for i in range(20,10,-1):
  print(i)

for i in range(1,21):
  if i%5==0:
    print(i)

for i in range(1,21):
  if i%5!=0:
    print(i)

"""#While loop"""

i = 0    #initialize
while i<10:     #condition
  print(i)
  i+=1      #Increament/decreament

i = 0    #initialize
while i<10:     #condition
  print("Hello")
  i+=1      #Increament/decreament

i=1
while i<=5:
  print("hello ", end="")

  j=1
  while j<=4:
    print("rocks ", end="")
    j+=1
i+=1
print()
