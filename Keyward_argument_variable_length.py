#keyward argument for variable lenght data

def person(name, **data):
    print(name)
    print(data)
person('Litesh', age=28, city='Pune', mobile=9179172701)


#keyward argument for variable lenght data
def person (name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('Litesh', age=28, city='Pune', mobile=9179172701)




#Global variable & local variable
a=10
print(id(a))
def something():
    a=15
    print("in term ", a)
    print(id(a))
something()

print("outside ", a)

#Make global variable inside the FUnction
a=10
print(id(a))
def something():
    a=5
    x=globals()['a']
    print(id(x))
    print("in FUnc ", a)
something()
print("outside ", a)

