#COnstructor, self and Comparing Objects

class computer:
    def _init_(self):
        self.name='Litesh'
        seif.age=28

c1=computer()
c2=computer()
c1.name='Upasna'
c2.age=24
print(c1.name)
#print(c2.name)
#print(c1.age)
print(c2.age)


#COnstructor, self and Comparing Objects

class computer:
    def _init_(self):
        self.name='Litesh'
        seif.age=28

    def update(self):
        self.age=30

c1=computer()
c2=computer()
c1.name='Upasna'
#c2.age=24
c1.update()
print(c1.name)
print(c1.age)

