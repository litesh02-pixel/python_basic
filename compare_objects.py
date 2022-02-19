#compare tweo objects

class computer:
    def __init__(self):
        self.name="Litesh"
        self.age=28

    def compare(self,other):
        if self.age==other.age:
            return true
        else:
            return false
c1=computer()
c2=computer()
c1.age=30
if c1.compare(c2):
    print("They are same")

else:
    print("They are different")

print(c1.name)
print(c2.name)
