x=["orange","apple","grapes"]
print(x.sort()) #sortsInAsc
for i in range(len(x)):
    print(x[i])
print("\n")

i=0
while i<(len(x)):
    print(x[i])
    i=i+1
print("\n")

[print(i) for i in x]  #shorthandForLoop

thislist = [100, 50, 65, 82, 23]
thislist.sort() #AscOrder
thislist.sort(reverse = True) #DescOrder
print(thislist)

thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist1 = ["orange", "mango", "Kiwi", "Pineapple", "banana"] #here K & P is cap
thislist.sort()
print(thislist)
mylist= thislist1.copy() #copying list way 1
mylist=list(thislist1)  #copying list way 2

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x) #joining 2 lists
print(list1)

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(0,11,2): #even nos
  print(x)

for x in range(1,11,2): #odd nos
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#----Nested loop---

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)










