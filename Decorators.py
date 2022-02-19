#Decorators

#simple code Divide(simpleCode)

def div(a,b):
    print(a/b)
div(5,4)
div(4,5)


#using Decorators

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner (a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
div1(2,4)
