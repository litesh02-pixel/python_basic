#Introduction to Polymorphism

#Duck Typing:

class IDLE:

    def execute(self):
        print("compiling")
        print("Running")

class laptop:
    def Code(self,ide):
        ide.execute()

ide=IDLE()
lap1=laptop()
lap1.Code(ide)


#second code

#class IDLE:
   # def execute(self):
     #   print("Compiling")
     #   print("Runnung")

class myeditor:
    def execute(self):
        print("spell check")
        print("conventinal check")
        print("compiling")
        print("running")
class laptop:
    def code(self,ide):
        ide.execute()

ide=myeditor()
lap1=laptop()
lap1.code(ide)
