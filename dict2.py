thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#thisdict["year"] = 2018 #way1 updation
#print(thisdict)
thisdict.update({"year":"2020"}) #way2 updation
thisdict.update({"color":"red"})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""thisdict.pop("model") #way1 deletion
print(thisdict)
del thisdict["model"] #way2 deletion
print(thisdict)"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #last item from list is removed
print(thisdict)

#del thisdict #deletes total dict
print(thisdict)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #clears the list items
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in thisdict.items():
  print(x,y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() #way1 to copy
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) #way2 to copy
print(mydict)

myfam={
  "child1":{
    "name":"surya",
    "age":27
  },

  "child2":{
    "name":"ramky",
    "age":24
  },
  "child3":{
    "name":"dippu",
    "age":23
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
