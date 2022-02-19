def update (x):
    #print(id(x))
    x=80
    #print(id(x))
    print("x ",x)
a=10
update(a)
print ("a ",a)
#print(id(a))



def update(lst):
    lst[0]=24
    print(id(lst))
    print("x ",lst)

lst=[12,20,30]
print(id(lst))
update(lst)
print("lst ",lst)



