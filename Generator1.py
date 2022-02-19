#Generator

def topten():

    yield 5
    yield 4
    yield 3
values=topten()
print(values.__next__())

for i in values:
    print(i)


#perfact square

def topten():

     n=1
     while n<=10:
        sq=n*n
        yield sq
        n+=1
values= topten()
for i in values:
    print(i)
