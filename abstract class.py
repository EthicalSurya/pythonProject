from abc import ABC,abstractmethod

# class computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
# class lappy(computer):
#
#     def process(self):
#         print("its running")

# com=computer()
# com.process()
# com1=lappy()
# com1.process()

class Shape(ABC):
    @abstractmethod
    def printarea(self):
         return area


class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=7
        self.breadth=7
    def printarea(self):
        return self.length*self.breadth

rect1=Rectangle()
print(rect1.printarea())
print(rect1.sides)

n= int(input("Enter any num"))

if n%3 is 0 and n%5 is 0:
    print("Zoom")
elif n%3 is 0:
    print("Zip")
elif n%5 is 0:
    print("Zap")
else:
    print("invalid")