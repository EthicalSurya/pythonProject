thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020  #overwrites the existing value
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=thisdict["model"] #Accessing Items way1
x=thisdict.get("model") #Accessing Items way2
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()  #to get keys
print(x) #before the change
car["color"] = "white"
print(x) #after the change

y=car.values()#to get values
print(y)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items() #The items() method will return each item in a dictionary, as tuples in a list.
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items() 
print(x) #before the change
car["color"] = "red"
print(x) #after the change
