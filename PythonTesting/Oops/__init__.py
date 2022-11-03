class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is",self.cpu,self.ram)

com1=computer('I5','I6')
com2=computer('ryan 3',8)

com1.config()
com2.config()