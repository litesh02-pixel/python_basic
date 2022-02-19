#factorial of a number

def fact(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return (f)

x=10
result=fact(x)
print(result)


#factorial of a number  using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(10)
print(result)
