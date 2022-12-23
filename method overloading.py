# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)

# Integer
add('int', 5, 6)
# String
add('str', 'Hi ', 'Geeks')

#--------------------------------------------

# USING DISPATCH

from multipledispatch import dispatch

# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result);


# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result);

# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result);

#calling product method with 2 arguments
product(2,3,2) #this will give output of 12
product(2.2,3.4,2.3) # this will give output of 17.985999999999997


# ---------------------------------Method Overriding------------------------------------------
class A:

	def fun1(self):
		print('feature_1 of class A')

	def fun2(self):
		print('feature_2 of class A')


class B(A):

	# Modified function that is
	# already exist in class A

	def fun1(self):
		print('Modified feature_1 of class A by class B')

	def fun3(self):
		print('feature_3 of class B')


# Create instance
obj = B()
obj1= A()
# Call the override function
obj.fun1()
obj1.fun1()

