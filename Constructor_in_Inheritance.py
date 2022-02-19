#constructor in Inheritance

class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1A working")

    def feature2(self):
        print("feature 2A working")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("feature 1B working")

    def feature4(self):
        print("feature 4B working")



a1 = B()
a1.feature1()
a1.feature4()
