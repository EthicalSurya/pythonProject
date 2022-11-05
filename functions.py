def my_add(a,b):
  """This is a funct to add two numbers"""
  print("sum is:",a+b)
  print(my_add.__doc__) # doc string

my_add(10,20)

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Appalla", "Madhu")
my_function("Appalla", "Surya")

def my_function(*kids): #Arbitary arg
  print("The youngest child is "+ kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(**kid):  #Arbitary keyword arg
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function() #Default parameter
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"] #Passing list as an arg
my_function(fruits)

def my_function(x):
  return 5 * x     #return values
print(my_function(3))
print(my_function(5))
print(my_function(9))

'''def factorial(k):
  if k==0 or k==1:
    return 1
  else:
    return k * factorial(k-1)
k=int(input("Enter K value"))
res=factorial(k)
print(res)'''

def shout(text):
  return text.upper()
#print(shout("hi"))
yell=shout
print(yell("hi"))




