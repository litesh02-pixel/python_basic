#create class and objects

class computer:
    def config(self):
        print("i5, 16gb,1TB")

a='8'
comp1=computer()   #calling the class
print(type(comp1))
print(type(a))



#create class and objects

class computer:
    def config(self):
        print ("i5, 16gb, 1TB")
com1=computer()         #calling the class
computer.config(com1)   #printing the output of the class
com1.config()           #"or" printing the output of the class


#create class and objects
class computer:
    def _init_(self):
        print("in init")

    def config(self):
        print("i5, 16gb, 1TB")

com1=computer()
#com2=computer()
com1.config()
com1._init_()
