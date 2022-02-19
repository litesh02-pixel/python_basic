#Fib for less than 100 value
def fib(x):
     a=0
     b=1
     if x<=0:
         print("in valid")
     elif x==0:
         print(a)
     else:
         print(a)
         print(b)
     for i in range(2,x):
         c=a+b
         a=b
         b=c
         if (c<=x):
            print(c)
x=int(input("Enter the number "))
fib(x)
