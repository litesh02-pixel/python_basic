def greet ():
    print("Hello")
    print('Good Morning')
greet()


def add(x,y):
    c=x+y
    d=x*y
    e=x/y
    f=x-y
    print(c)
    print(d)
    print(e)
    print(f)
add(3,4)


def add_sub(x,y):
    c=x+y
    d=x-y
    e=x*y
    return c,d,e
R1, R2, R3=add_sub(5,4)
print(R1,R2,R3)


