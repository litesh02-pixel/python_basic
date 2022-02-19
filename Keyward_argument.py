#actual argument
def person(name, age):
    print(name)
    print(age)
person('navin',28)



#keyward argument
def person(name, age):
    print(name)
    print(age)
person(name='navin',age=28)

#default argument
def person(name, age=28):
    print(name)
    print(age)
person('navin')

#variable length argument
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

sum(5,6,7,8,50)
