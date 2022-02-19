#pass list to a function(Even/odd count)

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
lst=[11,12,13,14,15,16,17,18,19,20,21]
even, odd=count(lst)
#print(even)
#print(odd)
print("Even:{} and odd:{}".format(even,odd))
