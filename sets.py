thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

thisset = {"apple", "banana", "cherry","apple"} #sets don't allow dupes
print(thisset)

thisset = set(("apple", "banana", "cherry"))# using set() constructor
# note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #adding set item
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #adding one set items into another set
print(thisset)

thisset = {"ball", "bat", "stumps"}
x=thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

thisset = {"apple", "banana", "cherry"}
thisset.clear() #deletes values in sets but not set
print(thisset)

thisset = {"apple", "banana", "cherry"}
# del thisset #deletes the total set
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
fruits=thisset.union(tropical) #The union() method returns a new set with all items from both sets
print(fruits)