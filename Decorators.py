#Passing the function as an argument
def shout(text):
  return text.upper()

def whisper(text):
  return text.lower()

def greet(func):
  # storing the function in a variable
  greeting = func("""Hi, I am created by a function passed as an argument.""")
  print(greeting)

greet(shout)
greet(whisper)

#Returning functions from another function.
def create_adder(x):
  def adder(y):
    return x + y

  return adder

add_15 = create_adder(15)
print(add_15(10))
#-----------------------------------------------------------------------

def sub(a,b):
  print(a-b)

def smart_sub(func):
  def inner(a,b):
    if a < b:
      a, b = b, a
    return func(a,b)
  return inner

sub=smart_sub(sub)
sub(2,4)



