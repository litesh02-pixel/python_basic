#inheritance

class A:
    def feature1(self):
        print("fearure1 working")

    def feature2(self):
        print("feature2 working")

class B(A):
    def feature3(self):
        print("feature3 working")

    def feature4(self):
        print("feature4 working")

class C(B):
    def feature5(self):
        print("feature5 working")

a1=A()
a1.feature1()
a1.feature2()

a2=B()
a2.feature3()
a2.feature4()

b1=C()
b1.feature5()


