class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is : ",self.cpu,self.ram)


com1 = Computer('i5',16)
com2 = Computer('i3','1TB')
com1.config()
com2.config()
