#change value and add values using MAP function

from functools import reduce
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0, nums))
doubles=list(map(lambda n:n*2,evens))
print(evens)
print(doubles)

sum=reduce(lambda a,b:a+b,doubles)
print(sum)
