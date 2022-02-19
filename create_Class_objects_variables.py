class computer:
    def _init_(self,CPU,RAM):
        self.CPU=CPU
        self.RAM=RAM

    def config(self):
        print("config is ", self.CPU, self.RAM)

com1=computer('i5',16)
com2=computer('ryzen 3',8)
com1.config()
com2.config()
