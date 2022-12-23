def topten(n):
  for i in range(1,n+1):
    yield i**2

y=topten(10)
print(list(y))

l=[16,17,19,21,22,26,24,31,39,44,54]

def count(l):
  even=0
  odd=0
  for i in l:
    if i%2 is 0:
      even+=1
    else:
      odd+=1
  return even,odd

e,o=count(l)
print(e,o)

num=int(input("Enter your number"))

if num is 1 or num is 0:
  print("enter other than 1 or 0")
else:
  for i in range(2, num):
    if num % i == 0:
      print(num, "is not prime")
      break

    else:
      print(num, "is prime")




