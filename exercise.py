def factorial(n):

    if n ==0 or n==1:
        return 1
    else:
        f = 1

        for i in range(1,n+1):
            f = f * i

    return f

fact=factorial(1)
print(fact)

# ------------Prime number----------------

num=int(input("Enter your number"))

for i in range(2,num):
    if num%i==0:
        print(num,"is not prime")
        break
else:                                  #for else used
    print(num, "is prime")

#--------------------------------------------------------------------------------------------
# class example:
#     pass
#
# eg=example()
#
# eg.name="surya"
# eg.age=28
# eg.loc='hyd'
#
# print(eg.name)

#----------with constructor we eliminate above code ---------------------------

# class example1:
#     def __init__(self,name,age,loc):
#         print("Hi this is constructor")
#         self.name=name
#         self.age=age
#         self.loc=loc
#     def print_details(self):
#         return f"name is {self.name},age is {self.age} & city is {self.loc}"
#
#
# eg1=example1("surya",27,'hyd')
# print(eg1.age)
#
# print(eg1.print_details())
# eg2=example1("harry",31,'Del')
# print(eg2.age)

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
# -----------------------------------------------------------------
def gen(n):
    for i in range(n):
        yield i ** 2
        i += 1


a=gen(7)
# for i in a:
#     print(i)

print(a.__next__())
print(a.__next__())

# ------------------iterable egs--------------------------------------
l="Surya"    #strings are iterable
itr=l.__iter__()
print(itr.__next__())
print(itr.__next__())

# m=5744 #nums are non iterable
# itr=m.__iter__()
# print(itr.__next__()) #raises error



