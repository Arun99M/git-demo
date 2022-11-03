class Car:

    wheel=4                             #class namespace/variable
    def __init__(self):
        self.mil=10                    #Instance variable/namespace
        self.com='BMW'                #Instance variable/namespace

c1 = Car()
c2 = Car()

c1.mil=8
Car.wheel=5
print(c1.mil,c1.com,Car.wheel)
print(c1.mil,c1.com,Car.wheel)