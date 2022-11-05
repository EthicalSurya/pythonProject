thistuple = ("apple", "banana", "cherry", "apple", "cherry") #allows dupes

#A tuple
thistuple =("apple",)#comma mandatory
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #accessing tuple
print(thistuple[1:3])

thistuple = ("apple", "banana", "cherry") #using membership opr
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

  x=("apple", "banana", "cherry") #changing Tuple Values By conv into list
  y=list(x)
  y[1]="kiwi"
  x=tuple(y)
  print(x)

  thistuple = ("apple", "banana", "cherry")
  y = list(thistuple)
  y.append("orange")
  thistuple = tuple(y)
  print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists