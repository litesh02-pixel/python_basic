#square of number

f=lambda a:a*a
result=f(19)
print(result)


#Addition/SUbtraction of number


f=lambda a,b:a+b
result=(f(5,4))
print(result)

#Using Lambda

def is_even(n):
    return n%2==0
nums=[3,2,4,5,6,7,8,10]
evens=list(filter(is_even,nums))
#evens=list(filter[lambda n:n%2==0,nums])
print(evens)
