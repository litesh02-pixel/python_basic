#method overloading 2


class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

S1 = student(58,34)
print(S1.sum(5))
print(S1.sum(5,6))
print(S1.sum(5,7,9))


#Mthod Overriding:

class A:
    def show(self):
        print("in A show")
#without over-riding
#class B(A):
    #pass
#method over-riding
class B(A):
    def show(self):
        print("in B show")
a1=B()
a1.show()
