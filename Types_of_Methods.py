#Different types of methods
#instance method

class student:

    school="COEP"
    print(school)
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

S1=student(43,37,45)
S2=student(44,56,54)
print(S1.avg())
print(S2.avg())


#Different types of methods
#Class method

class student:

    school="COEP"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student")
S1=student(35,39,59)
S2=student(36,48,56)
print(S1.avg())
print(S2.avg())
print(student.info())
student.info()
