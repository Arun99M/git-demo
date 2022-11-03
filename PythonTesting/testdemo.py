class calculator :
    num =100

    def __init__(self,a,b):
        self.firstnumber =a
        self.secondnumber =b
        print('i am called automatically when object is created')
    def getData(self):
        print('iam now execting as method in class')
    def summation(self):
        return(self.firstnumber + self.secondnumber + calculator.num)

obj = calculator(4,5)
obj.getData()
print(obj.summation())

obj1 = calculator(10,20)
obj1.getData()
print(obj1.summation())