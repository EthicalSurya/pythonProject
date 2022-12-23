
# Python program to show use of
# + operator for different purposes.
print(1 + 2)

# concatenate two strings
print("Geeks"+"For")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks"*4)



class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):  #DunderMethod
        print("let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("let's mul")
        return self.num * num2.num

n1=Number(4)
n2=Number(6)
sum=n1+n2    #Adding two instances using operator overloading
print(sum)
mul=n1*n2
print(mul)